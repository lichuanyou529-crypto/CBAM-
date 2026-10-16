const { JSDOM, VirtualConsole } = require("jsdom");
const fs = require("fs");
const path = require("path");

const DIR = "C:/Users/lichuanyou/WorkBuddy/2026-10-12-12-56-48/cbam-verifier-board";
const HTML = fs.readFileSync(path.join(DIR, "index.html"), "utf8");

function run(label, mode, cb) {
  const vc = new VirtualConsole();
  const errs = [];
  vc.on("jsdomError", e => errs.push("jsdomError: " + e.message));
  vc.on("error", (...a) => errs.push("console.error: " + a.join(" ")));

  const dom = new JSDOM(HTML, {
    runScripts: "dangerously",
    url: "http://example.com/index.html",
    virtualConsole: vc,
    beforeParse(window) {
      window.fetch = function (u) {
        if (String(u).indexOf("data.json") >= 0) {
          if (mode === "fail") return Promise.reject(new Error("boom"));
          const txt = fs.readFileSync(path.join(DIR, "data.json"), "utf8");
          return Promise.resolve({ ok: true, status: 200, json: () => Promise.resolve(JSON.parse(txt)) });
        }
        return Promise.resolve({ ok: false, status: 404, json: () => Promise.resolve({}) });
      };
    }
  });

  setTimeout(() => {
    const d = dom.window.document;
    const t = s => { const e = d.querySelector(s); return e ? e.textContent.trim() : "(缺失 " + s + ")"; };
    console.log("===== " + label + " =====");
    console.log("JS 错误        :", errs.length ? errs.join(" | ") : "无");
    console.log("状态胶囊       :", t("#live-chip"));
    console.log("数据基准日     :", t("#m-date"), "| 状态表:", t("#m-sop"));
    console.log("统计卡         : 官方", t("#s-official"), "已官宣", t("#s-announced"), "NAB", t("#s-nab"), "第三国", t("#s-tc"));
    console.log("机构榜提示     :", t("#v-count"));
    console.log("机构卡片数     :", d.querySelectorAll("#v-list .vcard").length);
    console.log("第一张卡标题   :", (d.querySelector("#v-list .vname") || {}).textContent);
    console.log("NAB 行数       :", d.querySelectorAll("#n-body tr").length);
    console.log("时间轴条数     :", d.querySelectorAll("#tl-list .tli").length);
    console.log("更新日志条数   :", d.querySelectorAll("#log-list .logrow").length);
    console.log("最近检查/倒计时:", t("#live-checked"), "/", t("#live-next"));
    console.log("②法规板块数   :", d.querySelectorAll("#reg-list .rgroup").length,
      "| 条目数:", d.querySelectorAll("#reg-list .rrow").length,
      "| 标题:", (d.querySelector("#reg-list .rg-t") || {}).textContent);
    console.log("③案例条目数   :", d.querySelectorAll("#case-list .rrow").length);
    console.log("④经验条目数   :", d.querySelectorAll("#tip-list .rrow").length);
    console.log("商机模块残留  :", d.getElementById("p10") || d.getElementById("bid-body") ? "仍存在（异常）" : "已移除");
    console.log("横幅残留      :", d.querySelector("main > .alert") ? "仍有顶部横幅（异常）" : "无");
    console.log("日历残留      :", d.getElementById("cal-grid") ? "仍存在（异常）" : "已移除");
    console.log("依据行残留    :", (d.querySelector("#case-list .srcs") ? "仍存在（异常）" : "已移除"));
    console.log("侧栏导航项数  :", d.querySelectorAll("aside.side .navitem").length);
    console.log("评分维度数    :", d.querySelectorAll("#v-list .vcard .dim").length / Math.max(1, d.querySelectorAll("#v-list .vcard").length), "/ 卡");
    console.log("机构商务/标签 :", d.querySelectorAll("#v-list .vcard .kv").length >= 4 ? "已渲染" : "缺失");
    console.log("页脚免责声明  :", (d.querySelector("footer .disclaim") || {}).textContent ? "已渲染" : "缺失");
    console.log("toast          :", t("#toast") || "(空)");
    dom.window.close();
    cb();
  }, 800);
}

run("场景 A：能取到 data.json（线上模式）", "ok", () => {
  run("场景 B：取不到 data.json（回退内置快照）", "fail", () => process.exit(0));
});
