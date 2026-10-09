// i18n: English is in the HTML; other languages load from /locales/<lang>.json
// To add a language: create locales/xx.json and add "xx" to SUPPORTED and a button with data-lang="xx".
(function(){
  const SUPPORTED=['en','es'],root=document.body.dataset.root||'';
  const cache={};
  async function load(l){if(!cache[l])cache[l]=await (await fetch(root+'locales/'+l+'.json')).json();return cache[l]}
  window.BUREX_T=k=>(window.BUREX_DICT&&window.BUREX_DICT[k])||k;
  async function setLang(l){
    if(!SUPPORTED.includes(l))l='en';
    try{window.BUREX_DICT=await load(l)}catch(e){console.warn('Could not load language',l);l='en';window.BUREX_DICT=null}
    const d=window.BUREX_DICT;
    if(d){document.querySelectorAll('[data-i18n]').forEach(n=>{if(d[n.dataset.i18n])n.textContent=d[n.dataset.i18n]});
      const k=document.body.dataset.titleKey;document.title=k==='meta.title'?d[k]:d[k]+' | BUREX Studio';
      document.querySelector('meta[name=description]').content=d['meta.desc'];
      document.querySelector('meta[property="og:title"]').content=d['meta.title'];
      document.querySelector('meta[property="og:description"]').content=d['meta.desc']}
    document.documentElement.lang=l;
    document.querySelectorAll('.lang-switch button').forEach(b=>b.setAttribute('aria-pressed',b.dataset.lang===l));
    try{localStorage.setItem('burex-lang',l)}catch(e){}
  }
  document.querySelectorAll('.lang-switch button').forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
  let saved='en';try{saved=localStorage.getItem('burex-lang')||'en'}catch(e){}
  setLang(saved);
})();
