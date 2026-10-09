import json,re
L={}
def K(k,en,es): L[k]=(en,es)
K('meta.title','BUREX Studio | Web Design for Businesses','BUREX Studio | Diseño web para empresas')
K('meta.desc','BUREX Studio designs modern, fast websites that help businesses build trust and win more customers.','BUREX Studio crea sitios web modernos y rápidos que ayudan a las empresas a generar confianza y conseguir más clientes.')
for k,en,es in [('home','Home','Inicio'),('services','Services','Servicios'),('work','Work','Trabajos'),('process','Process','Proceso'),('about','About','Nosotros'),('faq','FAQ','FAQ'),('contact','Contact','Contacto'),('cta','Start a Project →','Iniciar un proyecto →')]: K('nav.'+k,en,es)
K('hero.title','Websites built to turn visitors into customers.','Sitios web creados para convertir visitantes en clientes.')
K('hero.sub','We design modern, high-performing websites that help businesses stand out, build trust, and turn online visitors into real opportunities.','Diseñamos sitios web modernos y de alto rendimiento que ayudan a las empresas a destacar, generar confianza y convertir visitantes en oportunidades reales.')
K('hero.cta2','Explore Our Work','Ver nuestros trabajos')
K('benefits.title','Your website should do more than look good.','Tu sitio web debe hacer más que verse bien.')
K('benefits.text','A website should help your business build trust and create opportunities. Every page we design has a clear purpose.','Un sitio web debe ayudar a tu negocio a generar confianza y crear oportunidades. Cada página que diseñamos tiene un propósito claro.')
B=[('Modern & Professional Design','Clean, polished visuals that reflect the quality of your business.','Diseño moderno y profesional','Visuales limpios y cuidados que reflejan la calidad de tu negocio.'),
('Mobile-First Experience','Built to work beautifully on phones before anything else.','Experiencia mobile-first','Pensado para funcionar perfectamente en el teléfono antes que nada.'),
('Fast & Optimized Performance','Lightweight pages that load quickly and keep visitors engaged.','Rendimiento rápido y optimizado','Páginas ligeras que cargan rápido y mantienen el interés de los visitantes.'),
('Conversion-Focused Structure','Clear layouts and calls to action that guide visitors to get in touch.','Estructura enfocada en conversión','Diseños claros y llamadas a la acción que guían al visitante a contactarte.')]
for i,b in enumerate(B,1): K(f'benefits.{i}.t',b[0],b[2]);K(f'benefits.{i}.d',b[1],b[3])
K('services.title','Digital solutions built around your business.','Soluciones digitales creadas para tu negocio.')
S=[('Custom Website Design','Modern, professional websites tailored to your business and its goals.','Diseño web a medida','Sitios web modernos y profesionales adaptados a tu negocio y sus objetivos.'),
('Landing Page Development','Focused pages designed to present your offer and encourage visitors to take action.','Desarrollo de landing pages','Páginas enfocadas que presentan tu oferta y animan a los visitantes a actuar.'),
('Responsive Web Development','Seamless experiences across desktops, tablets, and smartphones.','Desarrollo web responsive','Experiencias fluidas en computadoras, tablets y teléfonos.'),
('Website Redesign','Transform outdated websites into modern, functional digital experiences.','Rediseño web','Transformamos sitios desactualizados en experiencias digitales modernas y funcionales.'),
('SEO Foundations','Essential on-page optimization to help search engines understand your website.','Bases de SEO','Optimización esencial para ayudar a los buscadores a entender tu sitio.'),
('Website Maintenance','Ongoing support, updates, and improvements to keep your website working smoothly.','Mantenimiento web','Soporte, actualizaciones y mejoras continuas para que tu sitio funcione sin problemas.')]
for i,s in enumerate(S,1): K(f'services.{i}.t',s[0],s[2]);K(f'services.{i}.d',s[1],s[3])
K('services.cta','Discuss Your Project →','Hablemos de tu proyecto →')
K('work.title','Selected Work.','Trabajos seleccionados.')
K('work.note','These are concept projects created by BUREX Studio, not work for real clients.','Estos son proyectos conceptuales creados por BUREX Studio, no trabajos para clientes reales.')
K('work.badge','Concept Project','Proyecto conceptual');K('work.view','View Project →','Ver proyecto →')
W=[('Summit Roofing Co.','Roofing Website Concept','A concept website for a roofing company, built to generate quote requests.','Concepto de sitio web para una empresa de techos, pensado para generar solicitudes de presupuesto.','Concepto de sitio de techos'),
('Velocity Auto Detail','Automotive Website Concept','A concept website that showcases detailing services and encourages bookings.','Concepto de sitio web que muestra servicios de detailing y fomenta las reservas.','Concepto de sitio automotriz'),
('GreenLine Landscaping','Landscaping Website Concept','A concept website for a professional landscaping company.','Concepto de sitio web para una empresa profesional de paisajismo.','Concepto de sitio de paisajismo')]
for i,w in enumerate(W,1): K(f'work.{i}.c',w[1],w[4]);K(f'work.{i}.d',w[2],w[3])
K('process.title','From idea to launch.','De la idea al lanzamiento.')
P=[('Discovery','We learn about your business, your goals, and what your website needs to achieve.','Descubrimiento','Conocemos tu negocio, tus objetivos y lo que tu sitio necesita lograr.'),
('Design','We create a modern visual experience aligned with your brand.','Diseño','Creamos una experiencia visual moderna alineada con tu marca.'),
('Development','We turn the design into a responsive, functional, and optimized website.','Desarrollo','Convertimos el diseño en un sitio responsive, funcional y optimizado.'),
('Launch','We prepare your website for publication and help bring your new digital presence online.','Lanzamiento','Preparamos tu sitio para su publicación y te ayudamos a poner en línea tu nueva presencia digital.')]
for i,p in enumerate(P,1): K(f'process.{i}.t',p[0],p[2]);K(f'process.{i}.d',p[1],p[3])
K('about.title','Small studio. Big ambitions.','Estudio pequeño. Grandes ambiciones.')
K('about.text','BUREX Studio is an independent web design studio focused on creating modern digital experiences for businesses around the world. We believe great websites combine thoughtful design, functionality, and clear communication.','BUREX Studio es un estudio independiente de diseño web enfocado en crear experiencias digitales modernas para empresas de todo el mundo. Creemos que los grandes sitios web combinan diseño cuidado, funcionalidad y comunicación clara.')
K('about.loc','We work remotely from Uruguay.','Trabajamos de forma remota desde Uruguay.')
K('faq.title','Frequently Asked Questions.','Preguntas frecuentes.')
F=[('How do I start a project?','Simply complete our project inquiry form. We\'ll review your request and get back to you by email.','¿Cómo inicio un proyecto?','Completa nuestro formulario de consulta. Revisaremos tu solicitud y te responderemos por correo electrónico.'),
('Do you work with international clients?','Yes. We work remotely and welcome projects from businesses around the world.','¿Trabajan con clientes internacionales?','Sí. Trabajamos de forma remota y recibimos proyectos de empresas de todo el mundo.'),
('How long does a website take?','Timelines depend on the size and complexity of each project. We\'ll discuss an estimated schedule after reviewing your requirements.','¿Cuánto tarda un sitio web?','Los plazos dependen del tamaño y la complejidad de cada proyecto. Hablaremos de un cronograma estimado después de revisar tus requisitos.'),
('Can you redesign my existing website?','Yes. We can help modernize your website\'s design, structure, and user experience.','¿Pueden rediseñar mi sitio actual?','Sí. Podemos modernizar el diseño, la estructura y la experiencia de usuario de tu sitio.'),
('How do we communicate during the project?','Communication is primarily handled through email, making it easy to share updates, feedback, and project details.','¿Cómo nos comunicamos durante el proyecto?','La comunicación se realiza principalmente por correo electrónico, lo que facilita compartir avances, comentarios y detalles del proyecto.')]
for i,f in enumerate(F,1): K(f'faq.{i}.q',f[0],f[2]);K(f'faq.{i}.a',f[1],f[3])
C=[('title',"Let's build something great.",'Construyamos algo grandioso.'),('sub',"Tell us a little about your business and what you have in mind. We'll review your project and get back to you by email.",'Cuéntanos un poco sobre tu negocio y lo que tienes en mente. Revisaremos tu proyecto y te responderemos por correo electrónico.'),
('name','Full Name','Nombre completo'),('business','Business Name (optional)','Nombre del negocio (opcional)'),('email','Email Address','Correo electrónico'),('country','Country (optional)','País (opcional)'),
('service','What service do you need?','¿Qué servicio necesitas?'),('s1','New Website','Sitio web nuevo'),('s2','Website Redesign','Rediseño web'),('s3','Landing Page','Landing page'),('s4','Website Maintenance','Mantenimiento web'),('s5','Other','Otro'),
('hasSite','Do you currently have a website?','¿Tienes actualmente un sitio web?'),('yes','Yes','Sí'),('no','No','No'),('url','Website URL','URL del sitio'),
('project','Tell us about your project','Cuéntanos sobre tu proyecto'),('timeline','Preferred Timeline (optional)','Plazo preferido (opcional)'),('t1','As soon as possible','Lo antes posible'),('t2','Within a month','En un mes'),('t3','Flexible','Flexible'),('t4','Not sure yet','Aún no lo sé'),
('send','Send Project Inquiry →','Enviar consulta →'),('sending','Sending…','Enviando…'),
('privacy','We only use your details to reply to your inquiry. See our','Solo usamos tus datos para responder a tu consulta. Consulta nuestra'),('privacyLink','Privacy Policy','Política de privacidad'),
('alt','Prefer to email us directly?','¿Prefieres escribirnos directamente?'),('altBtn','Send an Email →','Enviar un correo →'),
('success','Thank you for reaching out! Your project inquiry has been sent successfully. We\'ll get back to you by email.','¡Gracias por escribirnos! Tu consulta se envió correctamente. Te responderemos por correo electrónico.'),
('error','Something went wrong and your inquiry was not sent. Your details are still here, so please try again.','Algo salió mal y tu consulta no se envió. Tus datos siguen aquí, inténtalo de nuevo.'),
('notConfigured','The form is not connected yet. Please email us directly instead.','El formulario aún no está conectado. Por favor escríbenos directamente por correo.'),
('eName','Please enter your name.','Escribe tu nombre.'),('eEmail','Please enter a valid email, like name@company.com.','Escribe un correo válido, por ejemplo nombre@empresa.com.'),('eProject','Please tell us briefly about your project.','Cuéntanos brevemente sobre tu proyecto.')]
for k,en,es in C: K('contact.'+k,en,es)
for k,en,es in [('tag','Web Design · Digital Solutions','Diseño web · Soluciones digitales'),('based','Based in Uruguay. Working worldwide.','Con base en Uruguay. Trabajando en todo el mundo.'),('privacy','Privacy Policy','Política de privacidad'),('rights','All rights reserved.','Todos los derechos reservados.')]: K('footer.'+k,en,es)
K('privacy.title','Privacy Policy','Política de privacidad')
K('privacy.p1','When you send our project inquiry form, we receive the details you enter: name, email, and project information, plus any optional fields you complete.','Cuando envías nuestro formulario de consulta, recibimos los datos que ingresas: nombre, correo y detalles del proyecto, además de los campos opcionales que completes.')
K('privacy.p2','We use this information only to reply to your inquiry and discuss your project. We do not sell your data.','Usamos esta información solo para responder a tu consulta y conversar sobre tu proyecto. No vendemos tus datos.')
K('privacy.p3','Form submissions are processed by Netlify Forms. To request deletion of your data, email us at the address shown in the footer.','Los envíos del formulario son procesados por Netlify Forms. Para solicitar la eliminación de tus datos, escríbenos al correo que aparece en el pie de página.')
K('privacy.p4','Draft text: have it reviewed before launch to match your form provider and local regulations.','Texto borrador: haz que lo revisen antes del lanzamiento para ajustarlo a tu proveedor de formularios y a la normativa local.')
json.dump({k:v[0] for k,v in L.items()},open('locales/en.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
json.dump({k:v[1] for k,v in L.items()},open('locales/es.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
def T(k,tag,cls='',x=''): return f'<{tag}{f" class=\"{cls}\"" if cls else ""} data-i18n="{k}"{x}>{L[k][0]}</{tag}>'
ICON=['<path d="M4 5h16v10H4zM8 19h8"/>','<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>','<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>','<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/>']
sec={}
sec['benefits']=f'<section id="benefits" class="benefits-section"><div class="container">{T("benefits.title","h2","reveal")}{T("benefits.text","p","section-text reveal")}<div class="card-grid four">'+''.join(f'<article class="card reveal"><svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">{ICON[i-1]}</svg>{T(f"benefits.{i}.t","h3")}{T(f"benefits.{i}.d","p")}</article>' for i in range(1,5))+'</div></div></section>'
sec['services']=f'<section id="services" class="services-section"><div class="container">{T("services.title","h2","reveal")}<div class="card-grid spaced">'+''.join(f'<article class="card reveal">{T(f"services.{i}.t","h3")}{T(f"services.{i}.d","p")}<a class="btn btn-secondary btn-small" href="CONTACT" data-i18n="services.cta">{L["services.cta"][0]}</a></article>' for i in range(1,7))+'</div></div></section>'
ids=['summit-roofing','velocity-auto','greenline']
sec['work']=f'<section id="work" class="portfolio-section"><div class="container">{T("work.title","h2","reveal")}{T("work.note","p","section-text reveal")}<div class="card-grid spaced">'+''.join(f'<article class="card reveal" id="{ids[i-1]}"><div class="project-thumb" role="img" aria-label="{W[i-1][1]} mockup"></div>{T("work.badge","span","badge")}<h3>{W[i-1][0]}</h3>{T(f"work.{i}.c","p","project-meta")}{T(f"work.{i}.d","p")}<a class="btn btn-secondary btn-small" href="PORTFOLIO#{ids[i-1]}" data-i18n="work.view">{L["work.view"][0]}</a></article>' for i in range(1,4))+'</div></div></section>'
sec['process']=f'<section id="process" class="process-section"><div class="container">{T("process.title","h2","reveal")}<ol class="steps spaced">'+''.join(f'<li class="step reveal"><span class="step-number">0{i}</span>{T(f"process.{i}.t","h3")}{T(f"process.{i}.d","p")}</li>' for i in range(1,5))+'</ol></div></section>'
sec['about']=f'<section id="about" class="about-section"><div class="container">{T("about.title","h2","reveal")}{T("about.text","p","section-text tight")}{T("about.loc","p","about-location")}</div></section>'
sec['faq']=f'<section id="faq" class="faq-section"><div class="container">{T("faq.title","h2")}<div class="faq-list spaced">'+''.join(f'<div class="faq-item"><h3><button class="faq-question" aria-expanded="false" data-i18n="faq.{i}.q">{L[f"faq.{i}.q"][0]}</button></h3><div class="faq-answer"><div>{T(f"faq.{i}.a","p")}</div></div></div>' for i in range(1,6))+'</div></div></section>'
def fld(i,k,typ='text',req=False,ac=''):
    return f'<div class="field"><label for="{i}" data-i18n="contact.{k}">{L["contact."+k][0]}</label><input id="{i}" name="{NAMES[i]}" type="{typ}"{" required" if req else ""}{f" autocomplete=\"{ac}\"" if ac else ""}>'+(f'<span class="field-error" id="{i}-error" role="alert"></span>' if req else '')+'</div>'
NAMES={'name':'Full Name','business':'Business Name','email':'email','country':'Country','siteUrl':'Current Website'}
def sel(i,k,nm,opts):
    return f'<div class="field"><label for="{i}" data-i18n="contact.{k}">{L["contact."+k][0]}</label><select id="{i}" name="{nm}">'+''.join(f'<option value="{L["contact."+o][0]}" data-i18n="contact.{o}">{L["contact."+o][0]}</option>' for o in opts)+'</select></div>'
sec['contact']=f'''<section id="contact" class="contact-section"><div class="container">{T("contact.title","h2")}{T("contact.sub","p","section-text")}
<form id="contact-form" class="contact-form" name="burex-contact" method="POST" action="/" data-netlify="true" netlify-honeypot="_gotcha" novalidate>
 <input type="hidden" name="form-name" value="burex-contact">
{fld("name","name","text",True,"name")}{fld("business","business","text",False,"organization")}{fld("email","email","email",True,"email")}{fld("country","country","text",False,"country-name")}
{sel("service","service","Service",["s1","s2","s3","s4","s5"])}
<div class="field"><label for="hasSite" data-i18n="contact.hasSite">{L["contact.hasSite"][0]}</label><select id="hasSite" name="Has Website"><option value="No" data-i18n="contact.no">No</option><option value="Yes" data-i18n="contact.yes">Yes</option></select></div>
<div class="field full" id="siteUrlField" hidden><label for="siteUrl" data-i18n="contact.url">{L["contact.url"][0]}</label><input id="siteUrl" name="Current Website" type="url" placeholder="https://"></div>
<div class="field full"><label for="project" data-i18n="contact.project">{L["contact.project"][0]}</label><textarea id="project" name="Project Details" required></textarea><span class="field-error" id="project-error" role="alert"></span></div>
{sel("timeline","timeline","Timeline",["t1","t2","t3","t4"])}
<div class="visually-hidden" aria-hidden="true"><label>Leave empty<input name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
<p class="form-note full"><span data-i18n="contact.privacy">{L["contact.privacy"][0]}</span> <a href="PRIVACY" data-i18n="contact.privacyLink">{L["contact.privacyLink"][0]}</a>.</p>
<p class="full" hidden></p>
<div class="form-actions"><button class="btn btn-primary" id="submit-btn" type="submit" data-i18n="contact.send">{L["contact.send"][0]}</button></div>
<p class="form-status" id="form-status" role="status" aria-live="polite"></p>
</form>
<div class="alt-contact"><span data-i18n="contact.alt">{L["contact.alt"][0]}</span> <a class="btn btn-secondary btn-small" id="mailto-btn" href="mailto:" data-i18n="contact.altBtn">{L["contact.altBtn"][0]}</a></div></div></section>'''
sec['contact']=sec['contact'].replace('<p class="full" hidden></p>\n','')
sec['privacy']='<section class="privacy-section"><div class="container prose">'+''.join(T(f"privacy.p{i}","p","section-text") for i in range(1,5))+'</div></section>'
sec['hero']=f'''<section id="home" class="hero-section"><div class="hero-grid" aria-hidden="true"></div><div class="container hero-content">
{T("hero.title","h1")}{T("hero.sub","p","lead")}
<div class="hero-actions"><a class="btn btn-primary" href="CONTACT" data-i18n="nav.cta">{L["nav.cta"][0]}</a><a class="btn btn-secondary" href="PORTFOLIO" data-i18n="hero.cta2">{L["hero.cta2"][0]}</a></div></div></section>'''
FAV="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Crect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%236366f1%22/%3E%3Ctext x=%2216%22 y=%2222%22 font-size=%2218%22 font-weight=%22700%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22sans-serif%22%3EB%3C/text%3E%3C/svg%3E"
def page(fn,title,body,root,titlekey,home=False):
    r=root; idx=('' if home else r+'index.html')
    nav=''.join(f'<li><a href="{idx}#{a}" data-i18n="nav.{k}">{L["nav."+k][0]}</a></li>' for k,a in [('home','home'),('services','services'),('work','work'),('process','process'),('about','about'),('faq','faq'),('contact','contact')])
    cta=f'{idx}#contact' if home else f'{r}index.html#contact'
    h=f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{L['meta.desc'][0]}">
<meta property="og:title" content="{L['meta.title'][0]}"><meta property="og:description" content="{L['meta.desc'][0]}"><meta property="og:type" content="website">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{r}css/style.css"><link rel="stylesheet" href="{r}css/responsive.css"><link rel="stylesheet" href="{r}css/animations.css"></head>
<body data-root="{r}" data-title-key="{titlekey}">
<header class="navbar"><div class="container navbar-inner"><a class="logo" href="{r}index.html" aria-label="BUREX Studio">BUREX<small>STUDIO</small></a>
<nav aria-label="Main"><ul class="nav-menu" id="nav-menu">{nav}<li><a class="btn btn-primary btn-small" href="{cta}" data-i18n="nav.cta">{L['nav.cta'][0]}</a></li></ul></nav>
<div class="nav-actions"><div class="lang-switch" role="group" aria-label="Language"><button type="button" data-lang="en">EN</button><button type="button" data-lang="es">ES</button></div>
<button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Menu"><span></span><span></span><span></span></button></div></div></header>
<main id="main">{body}</main>
<footer class="footer"><div class="container footer-inner"><div><strong>BUREX Studio</strong><p data-i18n="footer.tag">{L['footer.tag'][0]}</p><p><a id="footer-email" href="mailto:"></a></p></div>
<ul class="footer-links"><li><a href="{idx}#home" data-i18n="nav.home">Home</a></li><li><a href="{idx}#services" data-i18n="nav.services">Services</a></li><li><a href="{idx}#work" data-i18n="nav.work">Work</a></li><li><a href="{idx}#about" data-i18n="nav.about">About</a></li><li><a href="{idx}#contact" data-i18n="nav.contact">Contact</a></li><li><a href="{r}pages/privacy.html" data-i18n="footer.privacy">Privacy Policy</a></li></ul>
<p>© <span id="year"></span> BUREX Studio. <span data-i18n="footer.rights">{L['footer.rights'][0]}</span><br><span data-i18n="footer.based">{L['footer.based'][0]}</span></p></div></footer>
<script src="{r}js/config.js"></script><script src="{r}js/navigation.js"></script><script src="{r}js/animations.js"></script><script src="{r}js/translations.js"></script><script src="{r}js/main.js"></script><script src="{r}js/contact.js"></script></body></html>'''
    h=h.replace('href="CONTACT"',f'href="{"#contact" if home else r+"index.html#contact"}"').replace('href="PORTFOLIO#',f'href="{r}pages/portfolio.html#').replace('href="PORTFOLIO"',f'href="{"#work" if home else r+"index.html#work"}"').replace('href="PRIVACY"',f'href="{r}pages/privacy.html"')
    open(fn,'w',encoding='utf8').write(h)
def hero(k): return f'<section class="page-hero"><div class="container">{T(k,"h1")}</div></section>'
page('index.html',L['meta.title'][0],''.join(sec[s] for s in ['hero','benefits','services','work','process','about','faq','contact']),'','meta.title',True)
for fn,key,secs in [('services','nav.services',['services']),('portfolio','nav.work',['work']),('about','nav.about',['about']),('contact','nav.contact',['contact'])]:
    page(f'pages/{fn}.html',L[key][0]+' | BUREX Studio',hero(key)+''.join(sec[s] for s in secs),'../',key)
page('pages/privacy.html',L['privacy.title'][0]+' | BUREX Studio',hero('privacy.title')+sec['privacy'],'../','privacy.title')
