import os
import re
import json
from pathlib import Path

SKILLS_DIR = Path("C:/Users/shahin.karimov/.gemini/config/skills")
OUTPUT_JSON = Path("C:/Users/shahin.karimov/.gemini/config/skills_manifest.json")
OUTPUT_MD = Path("C:/Users/shahin.karimov/.gemini/config/skills_index.md")

# Comprehensive Category Taxonomy
CATEGORIES = {
    "🤖 AI Agents, Swarms & Orchestration": [
        "agent", "swarm", "orchestrat", "subagent", "autonomous", "browser-use",
        "ufo", "composio", "superpowers", "openclaw", "crewai", "langchain", "autogen", "copilotkit"
    ],
    "🎨 Web Frontend, UI/UX & Design Systems": [
        "react", "next", "vue", "tailwind", "css", "html", "ui-ux", "taste-skill",
        "frontend", "animation", "motion", "d3", "canvas", "shadcn", "threejs",
        "design-system", "deck", "presentation", "svg", "web-design", "icon", "dashboard",
        "anti-slop", "lucide", "rough-js", "figma"
    ],
    "☁️ Backend, APIs, Cloud & Databases": [
        "api", "graphql", "rest", "backend", "fastapi", "django", "node", "express",
        "postgres", "supabase", "redis", "database", "sql", "bigquery", "docker",
        "kubernetes", "terraform", "auth", "jwt", "oauth", "stripe", "payment",
        "rabbitmq", "kafka", "cdc", "grpc", "websockets"
    ],
    "🛡️ Cybersecurity, Pentesting & Vulnerability Audits": [
        "security", "audit", "pentest", "vulnerability", "attack", "exploit",
        "hunt-", "offensive-", "idor", "xss", "sqli", "rce", "ssrf", "strix",
        "red-team", "threat", "soc2", "compliance", "privesc"
    ],
    "🎬 Media, Video, Audio & Image AI": [
        "video", "audio", "image", "speech", "tts", "whisper", "remotion", "ffmpeg",
        "yt-dlp", "elevenlabs", "suno", "runway", "stable-diffusion", "midjourney",
        "dall-e", "opencut", "funclip", "clipsai", "whisperx", "opencv"
    ],
    "⚡ Automation, Workflows & Tools": [
        "automation", "workflow", "-automation", "n8n", "zapier", "make-com",
        "slack", "discord", "gmail", "notion", "airtable", "scrape", "tavily",
        "firecrawl", "crawler", "playwright", "puppeteer"
    ],
    "📈 Trading, Finance & Algorithmic Markets": [
        "trading", "trade", "stock", "screener", "finance", "crypto", "dividend",
        "backtest", "finviz", "trendspider", "metatrader", "futures", "options"
    ],
    "📱 Mobile & Multiplatform Development": [
        "flutter", "dart", "react-native", "expo", "android", "swift", "ios",
        "xcode", "compose", "mobile", "tauri", "electron", "pake"
    ],
    "🎮 Game Development & 3D": [
        "game", "godot", "unity", "unreal", "phaser", "pixi", "pygame", "bevy",
        "shader", "tilemap", "ecs", "3d", "blender", "pixelfx", "typegpu"
    ],
    "🔬 Data Science, ML & Specialized Engineering": [
        "ml", "data", "spark", "dbt", "dataform", "bigframes", "analytics",
        "eval", "vector", "rag", "notebook", "statistics", "biology", "genom",
        "protein", "inferssd", "quantisation", "llama-cpp", "gguf", "deepseek"
    ]
}

CORE_24_SET = {
    "token-budget-advisor", "compact-conversation", "ai-session-optimizer",
    "prompt-caching-strategy", "clean-code", "anti-slop-ui",
    "memory-safety-patterns", "file-system-memory", "error-handling-patterns",
    "verification-loop", "gateguard", "zero-hallucination-coder",
    "code-simplification", "security-best-practices", "universal-skill-router",
    "session-guard", "work_efficiently", "work-efficiently", "git-safety-net",
    "locked-references", "written-gates-generation", "inferssd", "typegpu",
    "continuous-learning", "planning-with-files"
}

def classify(name: str, desc: str) -> str:
    if name in CORE_24_SET or name.replace("_", "-") in CORE_24_SET:
        return "🧠 Core 24 Mandatory Always-Active Guardrails"
    combined = (name + " " + desc).lower()
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in combined:
                return cat
    return "⚙️ Specialized Engineering & Utilities"

def main():
    skills = []
    
    for item in sorted(SKILLS_DIR.iterdir()):
        if not item.is_dir():
            continue
        skill_md = item / "SKILL.md"
        if not skill_md.exists():
            continue
            
        try:
            content = skill_md.read_text(encoding="utf-8", errors="ignore")
            name = item.name
            desc = ""
            
            # Simple frontmatter parser
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm = parts[1]
                    desc_match = re.search(r'description:\s*(?:[>|]-?\s*)?(.*?)(?=\n[a-zA-Z0-9_-]+:|\Z)', fm, re.DOTALL)
                    if desc_match:
                        raw_desc = desc_match.group(1).strip()
                        desc = " ".join([line.strip() for line in raw_desc.splitlines() if line.strip()])
                        desc = desc.strip('"\'')
            
            if not desc:
                lines = content.splitlines()
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith("#") and not line.startswith("---"):
                        desc = line
                        break
                        
            category = classify(name, desc)
            
            skills.append({
                "name": name,
                "description": desc[:300] if desc else f"Specialized skill for {name}.",
                "category": category,
                "path": str(skill_md).replace("\\", "/")
            })
        except Exception as e:
            print(f"Error reading {item.name}: {e}")

    print(f"Total skills indexed: {len(skills)}")
    
    # Write JSON manifest
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)
    print(f"Saved manifest to {OUTPUT_JSON}")
    
    # Also save copy to repo
    repo_manifest = Path("C:/Users/shahin.karimov/claude-skills/skills_manifest.json")
    with open(repo_manifest, "w", encoding="utf-8") as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)
    
    # Write Markdown index
    by_category = {}
    for s in skills:
        by_category.setdefault(s["category"], []).append(s)
        
    md_lines = [
        "# 🧠 Master Skill Catalog & Universal Auto-Router Index",
        f"\nTotal Active Skills: **{len(skills)}**\n",
        "This catalog is the single source of truth for all skills available to AI agents (Claude Code, Antigravity, Cursor, Codex). "
        "When executing any task, the Universal Auto-Router matches the exact skills, loads their instructions, and enforces production guardrails.\n"
    ]
    
    for cat, items in sorted(by_category.items()):
        md_lines.append(f"## {cat} ({len(items)} skills)\n")
        md_lines.append("| Skill Name | Description | Link |")
        md_lines.append("| :--- | :--- | :--- |")
        for item in items:
            name = item["name"]
            desc = item["description"].replace("|", "\\|")
            path = item["path"]
            md_lines.append(f"| **`{name}`** | {desc} | [`SKILL.md`](file:///{path}) |")
        md_lines.append("\n")
        
    OUTPUT_MD.write_text("\n".join(md_lines), encoding="utf-8")
    
    repo_index = Path("C:/Users/shahin.karimov/claude-skills/skills_index.md")
    repo_index.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Saved Markdown index to {OUTPUT_MD} and {repo_index}")

if __name__ == "__main__":
    main()
