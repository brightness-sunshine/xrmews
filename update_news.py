import os

def update_live_news():
    news_items = [
        {
            "title": "John Deere Launches XR Training System",
            "summary": "At CONEXPO-CON/AGG 2026, John Deere debuted a portable VR/AR training suite using Quest 3 and Pico 4 Ultra for heavy machinery.",
            "url": "https://www.deere.com/en/news/",
            "tag": "Industrial"
        },
        {
            "title": "EON Reality Taps Genie 3 AI for 3D Worlds",
            "summary": "EON Sentient has launched, leveraging Google DeepMind's Genie 3 to create photorealistic training environments for over 150 career paths.",
            "url": "https://eonreality.com",
            "tag": "Education"
        },
        {
            "title": "China Targets 25 Million XR Units by Year End",
            "summary": "The nation's five-year plan aims for massive market growth, backing 100 core companies to strengthen the global XR supply chain.",
            "url": "https://www.scmp.com/tech",
            "tag": "Global"
        }
    ]
    
    html_content = "<!-- Start of news items -->"
    for item in news_items:
        html_content += f"""
            <div class="card">
                <div class="card-body">
                    <span class="card-tag">{item['tag']}</span>
                    <h3 class="card-h">{item['title']}</h3>
                    <p class="card-p">{item['summary']}</p>
                    <a href="{item['url']}" target="_blank" style="color: var(--primary); font-weight: bold; text-decoration: none; font-size: 0.9rem;">Read More →</a>
                </div>
            </div>
        """
    html_content += "<!-- End of news items -->"
    
    with open('xrmews_repo/index.html', 'r') as f:
        content = f.read()
    
    # Check for placeholder or old news block
    if '<!-- Start of news items -->' in content:
        start_idx = content.find('<!-- Start of news items -->')
        end_idx = content.find('<!-- End of news items -->') + len('<!-- End of news items -->')
        new_content = content[:start_idx] + html_content + content[end_idx:]
    else:
        # Fallback for the first injection
        placeholder = '<div class="card" style="padding: 2rem; border-style: dashed; opacity: 0.7;">\n                    <p class="card-p">Fetching latest transmissions from the metaverse...</p>\n                </div>'
        new_content = content.replace(placeholder, html_content)
    
    with open('xrmews_repo/index.html', 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    update_live_news()
