git push报错

## 报错信息
```bash
Enumerating objects: 32, done.
Counting objects: 100% (32/32), done.
Delta compression using up to 16 threads
Compressing objects: 100% (28/28), done.
Writing objects: 100% (30/30), 9.44 MiB | 241.62 MiB/s, done.
Total 30 (delta 2), reused 30 (delta 2), pack-reused 0
error: RPC failed; HTTP 408 curl 56 Recv failure: Connection was reset
send-pack: unexpected disconnect while reading sideband packet
fatal: the remote end hung up unexpectedly
Everything up-to-date
```


## 解决方法
退出Github账号重新登陆


## 参考资料
https://stackoverflow.com/questions/70688399/send-pack-unexpected-disconnect-while-reading-sideband-packet-when-pushing-to-l

This is a very unsatisfactory follow-up, but may be helpful to posterity...  
I encountered the same error as OP (also on Windows), but simply deleting saved credential as above did not resolve it for me.  
But then I logged out of _Github_ and back in, and, voila, the next `git push` worked!

I observe that Github announced [beta support for passkeys](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/) recently and I had not pushed anything since then. I didn't sign up for the beta or make any other change on Github, but _post hoc, ergo propter hoc_?
