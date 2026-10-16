// 校验 V4 布局的 DOM 嵌套是否正确
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const file = path.join(__dirname, '..', 'index.html');
const html = fs.readFileSync(file, 'utf-8');
const dom = new JSDOM(html, { runScripts: 'outside-only' });
const d = dom.window.document;

const q = (s) => d.querySelector(s);
const ok = (label, cond, extra) => console.log((cond ? 'PASS' : 'FAIL') + '  ' + label + (extra ? '  → ' + extra : ''));

const shell = q('.shell');
ok('.shell 存在', !!shell);
ok('.side 是 .shell 直接子元素', shell && shell.querySelector(':scope > aside.side'));
ok('.maincol 是 .shell 直接子元素', shell && shell.querySelector(':scope > .maincol'));
ok('hero 在 .maincol 内', !!q('.maincol > header.hero'));
ok('main.wrap 在 .maincol 内', !!q('.maincol > main.wrap'));
ok('footer 在 .maincol 内', !!q('.maincol > footer'));
ok('footer 在 .maincol 末尾（其后无 section/panel）', (() => {
  const kids = [...q('.maincol').children];
  const fi = kids.findIndex(k => k.tagName === 'FOOTER');
  return fi >= 0 && !kids.slice(fi + 1).some(k => k.tagName === 'SECTION');
})());

const navs = [...d.querySelectorAll('aside.side .navitem')];
ok('侧边栏导航项数 = 5', navs.length === 5, navs.length + ' 个');
ok('侧边栏导航项均带 data-t', navs.every(n => n.dataset.t));
ok('侧边栏导航项均带 class tab（复用切换逻辑）', navs.every(n => n.classList.contains('tab')));
ok('默认激活项为 p1', navs.filter(n => n.classList.contains('on')).map(n => n.dataset.t).join() === 'p1');

ok('侧栏基准日占位存在', !!q('#side-date'));
ok('页脚二维码位存在', !!q('#qr'));

// 标签闭合粗查：div 开合数量一致
const openDiv = (html.match(/<div\b/g) || []).length;
const closeDiv = (html.match(/<\/div>/g) || []).length;
ok('div 开合数量一致', openDiv === closeDiv, openDiv + ' / ' + closeDiv);

// 面板与导航 target 对齐
const ids = navs.map(n => n.dataset.t);
const missing = ids.filter(id => !d.getElementById(id));
ok('导航 target 面板均存在', missing.length === 0, missing.join() || '无缺失');
