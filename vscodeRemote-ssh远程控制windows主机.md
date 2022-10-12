# 1 环境配置
用ssh连接时，本地称为client，远程主机称为host。

## 1.1 从 Windows Server 2019 或 Windows 10 1809 上的“设置”UI 安装 OpenSSH
OpenSSH 客户端和服务器是 Windows 10 1809 的可安装功能。

若要安装 OpenSSH，请启动“设置”，然后转到“应用”>“应用和功能”>“管理可选功能”。

扫描此列表，查看 OpenSSH 客户端是否已安装。 如果没有，则在页面顶部选择“添加功能”，然后：

若要安装 OpenSSH 客户端，请找到“OpenSSH 客户端”，然后单击“安装”。
若要安装 OpenSSH 服务器，请找到“OpenSSH 服务器”，然后单击“安装”。
安装完成后，请返回“应用”>“应用和功能”>“管理可选功能”，你应当会看到列出的 OpenSSH 组件。

## 1.2 使用 PowerShell 安装 OpenSSH
若要使用 PowerShell 安装 OpenSSH，请先以管理员身份运行 PowerShell。 为了确保 OpenSSH 可用，请运行以下 cmdlet：
```
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```

如果两者均尚未安装，则此操作应返回以下输出：
```
Name  : OpenSSH.Client~~~~0.0.1.0
State : NotPresent

Name  : OpenSSH.Server~~~~0.0.1.0
State : NotPresent
```

然后，根据需要安装服务器或客户端组件：
```
# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```

这两者应该都会返回以下输出：
```
Path          :
Online        : True
RestartNeeded : False
```

## 1.3 SSH 服务器的初始配置
若要配置 OpenSSH 服务器以在 Windows 上首次使用，请以管理员身份启动 PowerShell

在搜索框中搜索powershell，单击“以管理员身份运行”，

然后运行以下命令来启动 SSHD 服务：
```
Start-Service sshd
# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'
# Confirm the Firewall rule is configured. It should be created automatically by setup. 
Get-NetFirewallRule -Name *ssh*
# There should be a firewall rule named "OpenSSH-Server-In-TCP", which should be enabled
# If the firewall does not exist, create one
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

在第一次登录之前，我们先来了解两个概念：username和servername/hostname。

在windows服务器中，username可以用你激活电脑时使用的用户名，即文件资源管理器中C:\Users\username的username。而servername则是“设置”>“系统”>“关于”里的“设备名称”

在 Windows 上安装 OpenSSH 服务器后，可以从安装了 SSH 客户端的任何 Windows 设备上使用 PowerShell 来快速测试它。 在 PowerShell 中，键入以下命令（注意此处的username和servername都是用远程主机的）：
```
Ssh username@servername
```

到任何服务器的第一个连接都将生成类似以下内容的消息：
```
The authenticity of host 'servername (10.00.00.001)' can't be established.
ECDSA key fingerprint is SHA256:(<a large string>).
Are you sure you want to continue connecting (yes/no)?
```

回答必须是“yes”或“no”。 回答 Yes 会将该服务器添加到本地系统的已知 ssh 主机列表中。

系统此时会提示你输入密码（也就是远程主机的开机密码）。 作为安全预防措施，密码在键入的过程中不会显示。

在连接后，你将看到类似于以下内容的命令 shell 提示符：
```
domain\username@SERVERNAME C:\Users\username>
```

Windows OpenSSH 服务器使用的默认 shell 是 Windows 命令行解释器。


# 2 在vscode中连接
To connect to a remote host for the first time, follow these steps:

Verify you can connect to the SSH host by running the following command from a terminal / PowerShell window replacing user@hostname as appropriate.
```
ssh user@hostname 
# Or for Windows when using a domain / AAD account 
ssh user@domain@hostname
```

打开vscode，打开Command Palette (F1/ctrl+shift+P) ，输入"Remote-SSH: Connect to Host..." 并选中，选择"+ Add New SSH Host..."，and use the same user@hostname as in 1.2。

After a moment, VS Code will connect to the SSH server and set itself up. VS Code will keep you up-to-date using a progress notification and you can see a detailed log in the `Remote - SSH` output channel.

After you are connected, you'll be in an empty window. You can always refer to the Status bar to see which host you are connected to.

Clicking on the Status bar item will provide a list of remote commands while you are connected.

You can then open any folder or workspace on the remote machine using File > Open... or File > Open Workspace... just as you would locally!


# 3 摆脱密码——OpenSSH 密钥管理
Windows 环境中的大多数身份验证都是使用用户名-密码对完成的。 这适用于共享公共域的系统。 当跨域工作时（例如在本地和云托管的系统之间），这会变得更加困难。

相比之下，Linux 环境通常使用公钥/私钥对来驱动身份验证。 OpenSSH 提供了工具来帮助支持此用途，具体如下：

- ssh-keygen，用于生成安全的密钥
- ssh-agent 和 ssh-add，用于安全地存储私钥
- scp 和 sftp，在首次使用服务器时安全地复制公钥文件

本文档概述了如何在 Windows 上使用这些工具开始使用 SSH 进行密钥身份验证。 如果你不熟悉 SSH 密钥管理，我们强烈建议你查看 NIST 文档 IR 7966，标题为“使用安全 Shell (SSH) 的交互和自动化访问管理的安全性”。

## 3.1 关于密钥对
密钥对指的是由特定的身份验证协议使用的公钥和私钥文件。

SSH 公钥身份验证使用不对称加密算法来生成两个密钥文件 – 一个为“私钥”文件，一个为“公钥”文件。 私钥文件等效于密码，在所有情况下都应当保护它们。 如果有人获取了你的私钥，则他们可以像你一样登录到你有权登录的任何 SSH 服务器。 公钥放置在 SSH 服务器上，并且可以共享，不会危害私钥的安全。

将密钥身份验证用于 SSH 服务器时，SSH 服务器和客户端会依据私钥来比较所提供的用户名的公钥。 如果无法依据客户端私钥验证公钥，则身份验证失败。

可以通过在生成密钥对时要求提供密码来通过密钥对实现多重身份验证（参见下文的密钥生成）。 在身份验证期间，会提示用户输入密码，将使用该密码以及 SSH 客户端上的私钥来对用户进行身份验证。

## 3.2 用户密钥生成
若要使用基于密钥的身份验证，首先需要为客户端生成一些公钥/私钥对。 通过 PowerShell 或 cmd，使用 ssh-keygen 生成一些密钥文件。
```
cd ~\.ssh\
ssh-keygen
```

这应当会显示如下某些内容（其中，“username”将替代为你的用户名）
```
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\username\.ssh\id_rsa):
```

你可以按 Enter 来接受默认值，或指定要在其中生成密钥的路径。 此时，系统会提示你使用密码来加密你的私钥文件。 密码可以与密钥文件一起工作来提供双重身份验证。 在此示例中，我们将密码留空。（以下只是个例子，你的密钥肯定和示例不同）
```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in C:\Users\username\.ssh\id_rsa.
Your public key has been saved in C:\Users\username\.ssh\id_rsa.pub.
The key fingerprint is: 
SHA256:OIzc1yE7joL2Bzy8!gS0j8eGK7bYaH1FmF3sDuMeSj8 username@server@LOCAL-HOSTNAME

The key's randomart image is:
+--[RSA 2048]--+
|        .        |
|         o       |
|    . + + .      |
|   o B * = .     |
|   o= B S .      |
|   .=B O o       |
|  + =+% o        |
| *oo.O.E         |
|+.o+=o. .        |
+----[SHA256]-----+
```

现在，你有了一个公钥/私钥 rsa 密钥对（.pub 文件是公钥，其余的是私钥）：
```
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        9/28/2018  11:09 AM           1679 id_rsa
-a----        9/28/2018  11:09 AM            414 id_rsa.pub
```

请记住，私钥文件等效于密码，应当采用与保护密码相同的方式来保护它。

## 3.3 部署公钥
若要使用上面创建的用户密钥，需要将公钥放置在服务器上的一个文本文件中，该文件名为 authorized_keys，位于 users\username.ssh. 下

遗憾的是 Windows 下目前还没有提供 ssh-copy-id 命令，需要手动把用户的公钥添加到远程主机系统中的用户的 authorized_keys 文件中。具体在运行 OpenSSH Server 的主机上的操作步骤如下：

### 3.3.1 在host家目录下创建 .ssh 目录
打开 PowerShell，进入host用户的家目录，用 mkdir 命令创建 .ssh 目录：
```
cd ~ 
mkdir .ssh
```

### 3.3.2 创建 authorized_keys 文件并加入公钥
在 PowerShell 中执行 notepad .ssh\authorized_keys 命令创建文本文件，把客户端的公钥复制到这个文件中并保存。

把文本文件的名称修改为 authorized_keys（就是去掉后缀，这一步也可以手动操作）。
```
notepad .ssh\authorized_keys
mv .\.ssh\authorized_keys.txt .\.ssh\authorized_keys
```

### 3.3.3 修改 ssh 服务的配置文件
以管理员权限打开 PowerShell，执行命令
```
notepad C:\ProgramData\ssh\sshd_config
```

用“#”注释掉配置文件中的最后两行然后保存：
```
#Match Group administrators 
#       AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
```

最后在服务管理器器中重启 OpenSSH SSH Server 服务（我并不知道怎样重启服务，于是只好重启电脑），然后客户端就可以通过公钥认证的方式登录到远程服务器了。

## 3.4 通过公钥认证的方式登录到远程服务器
在客户端打开powershell，执行
```
ssh username@servername -i id_rsa
```

无需输入密码，你将直接看到类似于以下内容的命令 shell 提示符：
```
domain\username@SERVERNAME C:\Users\username>
```

之后，可通过输入“exit”退出。

## 3.5 如果你在上一步遇到了问题...
如果报错是找不到id_rsa文件（但是你的C:\Users\username\.ssh\id_rsa确实存在），你可以尝试：

在远程主机上，以管理员权限打开 PowerShell，执行命令
```
notepad C:\ProgramData\ssh\sshd_config
```

去掉以下两行的注释符，并将状态改为yes
```
PubkeyAuthentication yes
PermitEmptyPasswords yes
```

添加
```
RSAAuthentication yes
```

并重启远程主机，重试连接。

其它报错请上网搜索

## 3.6 在vscode上通过公钥认证的方式登录到远程服务器
在Command Palette (F1/ctrl+shift+P) 中，输入"ssh open configuration" 并打开客户端（本地）的config文件，内容应该类似如下
```
Host name
  HostName hostname
  User username
```

在下面添加
```
 IdentityFile "C:\Users\username\.ssh\id_rsa"
```

注意添加的文本前面是有缩进的（你应该知道“username”应该换成什么吧）

下一次登录远程主机时，点击vscode左下角的绿色标志，选择connect to，选择你的远程主机，就可以轻松登录了。

## 内网穿透
给个链接自己看吧，挺好用的

[Sakura Frp](​www.natfrp.com/)

远程激活anaconda环境
添加环境：
```
C:\Users\Username\Anaconda3
C:\Users\Username\Anaconda3\Scrips
C:\Users\Username\Anaconda3\Library\bin
```

在anaconda prompt中输入以下命令
```
conda install -n root -c pscondaenvs pscondaenvs
```

在PowerShell（管理员）中输入
```
Set-ExecutionPolicy RemoteSigned
```

并确认
