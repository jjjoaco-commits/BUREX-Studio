document.getElementById('year').textContent=new Date().getFullYear();
(function(){
  const email=(window.BUREX_CONFIG||{}).CONTACT_EMAIL||'';
  const f=document.getElementById('footer-email');f.textContent=email;f.href='mailto:'+email;
})();
document.querySelectorAll('.faq-question').forEach(btn=>btn.addEventListener('click',()=>{
  const open=btn.getAttribute('aria-expanded')==='true';
  btn.setAttribute('aria-expanded',!open);btn.closest('.faq-item').querySelector('.faq-answer').classList.toggle('open',!open);
}));
