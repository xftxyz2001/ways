## 下载
[官网](https://code.visualstudio.com/)
- [下载页](https://code.visualstudio.com/Download)


## 安装
下一步下一步即可，**将VSCode添加到资源管理器上下文菜单可以方便以后使用**：
![1764685060910](image/安装VSCode1.106/1764685060910.jpg)

[VSCode使用一段时间后会占用大量C盘空间](./清理VSCode缓存.md)，可以使用 [CleanVSCode.bat](./CleanVSCode.bat) 脚本清理，为方便使用，可以将其置于 `~/.vscode/` 下。


---

VS Code可以登录GitHub账号同步设置和扩展。以下内容是当前机器在 **2026-08-26** 的配置快照，VS Code版本为 `1.134.0`。

## 配置

配置示例：[VSCodeUserSettings.json](./VSCodeUserSettings.json)

`settings.json` 支持带注释和尾随逗号的JSONC语法。仓库文件是个人配置快照，其中的本机路径需要根据实际安装位置调整。

## 当前安装的扩展

列表包含当前已安装的全部扩展，包括处于禁用状态的扩展。以下顺序根据 **2026-08-26** 的Visual Studio Marketplace安装量和加权评分综合排列，以安装量为主、评分为辅。

| 扩展 | 功能简介 |
| --- | --- |
| Python | 提供Python语言支持，并连接代码补全、调试、测试及环境管理能力。 |
| Python Debugger | 使用debugpy在VS Code中调试Python程序。 |
| Jupyter Keymap | 为Notebook提供与经典Jupyter相近的快捷键。 |
| Live Server | 启动支持自动刷新的本地Web开发服务器。 |
| Pylance | 为Python提供高性能代码补全、类型分析和导航。 |
| Jupyter Slide Show | 为Jupyter Notebook单元格配置幻灯片放映属性。 |
| Chinese (Simplified) Language Pack | 为VS Code界面提供简体中文本地化。 |
| Jupyter Cell Tags | 在Notebook中查看和编辑Jupyter单元格标签。 |
| C/C++ Extension Pack | 集成常用C/C++开发扩展，简化工具链安装。 |
| CMake Tools | 在VS Code中配置、构建、运行和调试CMake项目。 |
| C/C++ | 提供C/C++代码补全、导航和调试支持。 |
| WSL | 直接在Windows Subsystem for Linux环境中进行开发。 |
| Jupyter Notebook Renderers | 渲染Notebook中的图表、图片及其他富输出。 |
| ESLint | 在编辑器中检查JavaScript和TypeScript代码规范问题。 |
| Test Runner for Java | 在VS Code中运行和调试JUnit或TestNG测试。 |
| Maven for Java | 管理Maven项目、依赖、生命周期和常用命令。 |
| Debugger for Java | 为Java程序提供运行和调试能力。 |
| Prettier - Code formatter | 使用Prettier统一多种前端文件的代码格式。 |
| C/C++ Themes | 提供适配C/C++扩展的文件图标和颜色主题。 |
| Dev Containers | 在Docker容器中打开项目并使用完整的VS Code开发能力。 |
| Project Manager for Java | 管理Java项目、依赖和项目结构。 |
| Jupyter | 在VS Code中创建、运行和调试Jupyter Notebook。 |
| Remote - SSH: Editing Configuration Files | 提供SSH配置文件的编辑和语法支持。 |
| vscode-icons | 为资源管理器中的文件和目录提供图标主题。 |
| Remote Explorer | 集中查看和管理SSH、Tunnel等远程目标。 |
| Rainbow CSV | 高亮CSV/TSV列并提供查询、对齐和校验功能。 |
| Extension Pack for Java | 集成Java语言、调试、测试、Maven和项目管理扩展。 |
| Language Support for Java by Red Hat | 为Java提供代码补全、重构、格式化及Maven/Gradle支持。 |
| Path Intellisense | 在输入路径时自动补全文件和目录名称。 |
| Remote - SSH | 通过SSH在远程主机上打开目录并进行开发。 |
| Git Graph | 以图形方式查看Git提交、分支并执行常用操作。 |
| Markdown All in One | 提供Markdown快捷键、目录生成和编辑辅助。 |
| YAML | 提供YAML语法校验、补全和Kubernetes结构支持。 |
| Container Tools | 创建、管理和调试容器化应用。 |
| Error Lens | 将错误、警告和诊断信息直接突出显示在代码行中。 |
| Markdown Preview Enhanced | 提供支持图表、公式和导出的增强Markdown预览。 |
| Python Environments | 统一发现、创建、选择和管理Python环境。 |
| Spring Boot Tools | 为Spring Boot配置文件提供校验、补全和导航。 |
| GitHub Repositories | 无需本地克隆即可浏览和编辑GitHub仓库。 |
| Remote Repositories | 直接浏览和编辑远程Git仓库。 |
| Draw.io Integration | 在VS Code中创建和编辑Draw.io流程图。 |
| Spring Initializr Java Support | 通过Spring Initializr快速生成Spring Boot项目。 |
| Codex – OpenAI's coding agent | 在编辑器中使用Codex完成编码、理解和修改项目等任务。 |
| Image preview | 在代码边栏及悬停窗口中预览图片。 |
| Spring Boot Extension Pack | 集成常用Spring Boot开发扩展。 |
| Spring Boot Dashboard | 集中查看、启动、停止和调试Spring Boot应用。 |
| PlantUML | 编辑、预览和导出PlantUML图表。 |
| Vue (Official) | 为Vue单文件组件提供语言服务、补全和类型检查。 |
| Black Formatter | 使用Black格式化Python代码。 |
| C/C++ DevTools | 为C++开发提供增强的工程分析和开发工具。 |
| Office Viewer | 在VS Code中预览Office文件并编辑Markdown。 |
| Open | 使用操作系统默认程序打开当前文件。 |
| Add to GIT Ignore | 从资源管理器快速将文件或目录加入`.gitignore`。 |
| VSCode Shell-like Formatter | 格式化Shell、Dockerfile、`.gitignore`和`.env`等文件。 |

可以使用以下命令重新获取已安装扩展：

```powershell
code --list-extensions
```
