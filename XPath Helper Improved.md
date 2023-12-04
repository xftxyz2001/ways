## 下载
[下载地址](https://github.com/eliasdorneles/xpath_helper)

直接下载zip包，解压后，打开浏览器管理扩展选项卡，点击`加载解压缩的扩展`，选择解压后的文件夹即可。


## 快捷键修改
如果遇到快捷键冲突，可以通过修改如下文件来修改快捷键

`bar.js` 76行
```js
var handleKeyDown = function(e) {
  if (e.keyCode === X_KEYCODE && e.ctrlKey && e.shiftKey) { // !!!
    chrome.extension.sendMessage({'type': 'hideBar'});
  }
};
```

`content.js` 260行 280行
```js
xh.Bar.prototype.keyDown_ = function(e) {
  if (e.keyCode === xh.X_KEYCODE && e.ctrlKey && e.shiftKey) { // !!!
    if (!this.active_) {
      this.active_ = true;
      if (!this.barFrame_.parentNode) {
        // First bar request on this page. Add bar back to DOM.
        document.body.appendChild(this.barFrame_);
        // Use setTimeout so that the transition is visible.
        window.setTimeout(this.boundShowBar_, 0);
      } else {
        this.showBar_();
      }
    } else {
      this.hideBar_();
    }
  }

  // If the user just pressed Shift and they're not holding Ctrl, update query.
  // Note that we rely on the mousemove handler to have updated this.currEl_.
  // Also, note that checking e.shiftKey wouldn't work here, since Shift is the
  // key that triggered this event.
  if (this.active_ && e.keyCode === xh.SHIFT_KEYCODE && !e.ctrlKey) { // !!!
    this.updateQueryAndBar_(this.currEl_);
  }
};
```
