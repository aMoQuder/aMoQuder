import json

# Load projects
with open("projects.json", "r", encoding="utf-8") as file:
    projects = json.load(file)

# Start slider HTML
slider_html = """
<h2 align="center">🚀 My Projects Showcase</h2>

<div style="display:flex; overflow-x:auto; gap:20px; padding:10px;">
"""

# Generate each slide
for p in projects:
    slider_html += f"""
    <div style="
        min-width:300px;
        max-width:300px;
        background:#111;
        padding:15px;
        border-radius:14px;
        color:#fff;
        border:1px solid #444;
        text-align:center;
    ">
        <img src="{p['image']}" style="width:100%; border-radius:10px;"/>
        <h3>{p['title']}</h3>
        <p style="font-size:14px; color:#ccc;">{p['description']}</p>

        <div style="margin-top:10px;">
            <a href="{p['github']}">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" height="30">
            </a> &nbsp;
            {f'<a href="{p["youtube"]}"><img src="https://cdn-icons-png.flaticon.com/256/1384/1384060.png" height="30"></a>' if p["youtube"] else ""}
            &nbsp;
            {f'<a href="{p["linkedin"]}"><img src="https://www.iconpacks.net/icons/1/free-linkedin-icon-130-thumb.png" height="30"></a>' if p["linkedin"] else ""}
        </div>
    </div>
    """

# End
slider_html += "</div>"

# Save to README section
with open("SLIDER.md", "w", encoding="utf-8") as output:
    output.write(slider_html)
