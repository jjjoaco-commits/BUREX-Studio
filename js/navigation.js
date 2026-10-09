(function(){
  const t=document.querySelector('.nav-toggle'),m=document.getElementById('nav-menu'),bar=document.querySelector('.navbar');
  const set=o=>{m.classList.toggle('open',o);t.setAttribute('aria-expanded',o)};
  t.addEventListener('click',()=>set(!m.classList.contains('open')));
  m.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>set(false)));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')set(false)});
  const s=()=>bar.classList.toggle('scrolled',scrollY>20);addEventListener('scroll',s,{passive:true});s();
})();
