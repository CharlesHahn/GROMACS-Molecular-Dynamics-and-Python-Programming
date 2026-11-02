// Mermaid 前端渲染：把 Sphinx 输出的 <div class="highlight-mermaid"><pre> 内容交给 mermaid
(function () {
  "use strict";

  function mermaidReady() {
    return typeof mermaid !== "undefined";
  }

  function extractSource(pre) {
    // Sphinx/Pygments 输出 <pre><span></span>flowchart ...，取 pre 的纯文本即可
    var src = pre.textContent || "";
    return src.trim();
  }

  function renderAll() {
    var blocks = document.querySelectorAll("div.highlight-mermaid, pre.highlight-mermaid");
    if (!blocks.length) return;

    if (!mermaidReady()) {
      setTimeout(renderAll, 300);
      return;
    }

    mermaid.initialize({
      startOnLoad: false,
      theme: "default",
      flowchart: { useMaxWidth: true, htmlLabels: true, curve: "basis" },
      securityLevel: "loose",
      htmlLabels: true
    });

    blocks.forEach(function (block, idx) {
      var pre = block.tagName === "PRE" ? block : block.querySelector("pre");
      if (!pre) return;
      var src = extractSource(pre);
      if (!src) return;

      var id = "mermaid-" + idx;
      pre.id = id;
      pre.classList.add("mermaid-host");

      try {
        mermaid.render(id + "-svg", src).then(function (res) {
          pre.innerHTML = res.svg;
        }).catch(function (err) {
          pre.innerHTML = '<div class="mermaid-error">Mermaid 渲染失败：' + err + "</div>";
        });
      } catch (err) {
        pre.innerHTML = '<div class="mermaid-error">Mermaid 渲染失败：' + err + "</div>";
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderAll);
  } else {
    renderAll();
  }
})();