(function(){
  const form=document.getElementById('contact-form');if(!form)return;
  const status=document.getElementById('form-status'),btn=document.getElementById('submit-btn'),tr=k=>window.BUREX_T(k);
  const rules={name:v=>v.trim()?'':'contact.eName',
    email:v=>/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim())?'':'contact.eEmail',
    project:v=>v.trim()?'':'contact.eProject'};
  const check=el=>{const k=rules[el.id](el.value);el.classList.toggle('invalid',!!k);
    document.getElementById(el.id+'-error').textContent=k?tr(k):'';return !k};
  Object.keys(rules).forEach(id=>document.getElementById(id).addEventListener('blur',e=>check(e.target)));
  const has=document.getElementById('hasSite'),urlField=document.getElementById('siteUrlField');
  has.addEventListener('change',()=>{urlField.hidden=has.value!=='Yes'});
  const show=(k,cls)=>{status.textContent=tr(k);status.className='form-status '+cls};
  form.addEventListener('submit',async e=>{
    e.preventDefault();status.textContent='';
    if(!Object.keys(rules).map(id=>check(document.getElementById(id))).every(Boolean))return;
    btn.disabled=true;btn.textContent=tr('contact.sending');
    try{
      const data=new URLSearchParams(new FormData(form));
      const r=await fetch('/',{method:'POST',body:data,headers:{'Content-Type':'application/x-www-form-urlencoded'}});
      if(!r.ok)throw new Error(r.status);
      form.reset();urlField.hidden=true;show('contact.success','ok');   // success only after a confirmed response
    }catch(err){show('contact.error','err')}                           // data stays in the form for retry
    finally{btn.disabled=false;btn.textContent=tr('contact.send')}
  });
})();
