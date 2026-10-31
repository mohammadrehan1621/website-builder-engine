import os
import re

BASE_DIR = r"C:\Users\rehan\Desktop\projects\website_builder\Deployed_Websites\mohammadrehan.pages.dev"

def get_nav_html(active_page):
    def link_class(page_name):
        if page_name == active_page:
            return "text-slate-900 font-bold border-b-2 border-slate-900 pb-0.5 transition"
        return "hover:text-slate-900 transition"

    aegis_link = """<a class="hover:text-cyan-800 transition flex items-center gap-1.5 font-bold text-cyan-700 bg-cyan-50 hover:bg-cyan-100/80 px-2.5 py-1 rounded-lg border border-cyan-200/70" href="aegis.html">
<i class="w-3.5 h-3.5 text-cyan-600" data-lucide="shield"></i>
<span>RQL Aegis™</span>
<span class="bg-cyan-200/70 text-cyan-950 text-[10px] px-1.5 py-0.2 rounded font-extrabold">SOFTWARE</span>
</a>"""

    if active_page == 'aegis':
        aegis_link = """<a class="text-cyan-900 font-extrabold bg-cyan-100/90 px-2.5 py-1 rounded-lg border border-cyan-300 shadow-2xs flex items-center gap-1.5" href="aegis.html">
<i class="w-3.5 h-3.5 text-cyan-700" data-lucide="shield"></i>
<span>RQL Aegis™</span>
<span class="bg-cyan-200 text-cyan-950 text-[10px] px-1.5 py-0.2 rounded font-black">SOFTWARE</span>
</a>"""

    nav_links = f"""<nav class="hidden md:flex items-center gap-6 lg:gap-8 text-sm font-medium text-slate-600">
<a class="{link_class('home')}" href="index.html">Home</a>
<a class="{link_class('projects')}" href="projects.html">Projects</a>
{aegis_link}
<a class="{link_class('experience')}" href="experience.html">Experience</a>
<a class="hover:text-indigo-600 transition flex items-center gap-1 text-slate-600" href="https://rehanquantlab.substack.com" target="_blank" rel="noopener noreferrer">Research <i class="w-3 h-3" data-lucide="external-link"></i></a>
<a class="{link_class('contact')}" href="contact.html">Contact</a>
</nav>"""
    return nav_links

def get_right_cta():
    return """<div class="hidden lg:flex items-center gap-3">
<a class="p-2 text-slate-500 hover:text-slate-900 hover:bg-slate-100 rounded-xl transition" href="https://x.com/rehanquantlab" target="_blank" rel="noopener noreferrer" title="Follow Rehan Quant Lab on X">
<svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
</a>
<a class="text-slate-700 hover:text-slate-900 text-xs font-semibold px-3 py-2 rounded-xl border border-slate-200 hover:border-slate-300 bg-white transition flex items-center gap-1.5" href="Mohammad_Rehan_Resume.pdf" download>
<i class="w-3.5 h-3.5 text-slate-500" data-lucide="download"></i>
<span>Resume</span>
</a>
<a class="bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold px-4 py-2 rounded-xl shadow-sm transition flex items-center gap-2" href="contact.html#schedule-briefing">
<i class="w-3.5 h-3.5 text-emerald-300" data-lucide="calendar"></i>
<span>Schedule Briefing</span>
</a>
</div>"""

def update_file(filename, active_page):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: not found")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for <nav class="hidden md:flex ...">...</nav>
    pattern = r'<nav[^>]*class=["\'][^"\']*hidden md:flex[^"\']*["\'][^>]*>.*?</nav>'
    new_nav = get_nav_html(active_page)

    content, n_nav = re.subn(pattern, new_nav, content, count=1, flags=re.DOTALL)
    print(f"[{filename}] Nav replaced: {n_nav}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

pages = [
    ('index.html', 'home'),
    ('projects.html', 'projects'),
    ('experience.html', 'experience'),
    ('contact.html', 'contact'),
    ('legal.html', 'legal'),
]

for fname, active_page in pages:
    update_file(fname, active_page)

print("Navbar synchronization complete!")
