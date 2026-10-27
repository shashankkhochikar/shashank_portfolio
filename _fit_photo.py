from pathlib import Path
from PIL import Image, ImageEnhance

src = Path(
    r"C:\Users\Shashank Khochikar\.cursor\projects\d-PersonalWorkspace-SK-Portfolio-portfolio\assets"
    r"\c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_"
    r"fe61aafcd2eb7c83e1097057b6df90d2_images_Professional_South_Asian_Man_Headshot_"
    r"Cutout-addd9ea0-152c-4733-8f66-1733162df5d4.png"
)
out_dir = Path(r"d:\PersonalWorkspace\SK_Portfolio\portfolio\assets\img")
out_home = out_dir / "home-perfil.png"
out_about = out_dir / "about-perfil.png"

img = Image.open(src).convert("RGBA")
alpha = img.split()[-1]
bbox = alpha.getbbox()
pad = 24
x0, y0, x1, y1 = bbox
x0 = max(0, x0 - pad)
y0 = max(0, y0 - pad)
x1 = min(img.width, x1 + pad)
y1 = min(img.height, y1 + pad)
subject = img.crop((x0, y0, x1, y1))

TW, TH = 800, 937
canvas = Image.new("RGBA", (TW, TH), (0, 0, 0, 255))

sw, sh = subject.size
scale = min((TW * 0.94) / sw, (TH * 0.98) / sh)
nw, nh = int(sw * scale), int(sh * scale)
subject_r = subject.resize((nw, nh), Image.Resampling.LANCZOS)

rgb = subject_r.convert("RGB")
rgb = ImageEnhance.Contrast(rgb).enhance(1.04)
rgb = ImageEnhance.Color(rgb).enhance(1.03)
subject_r = Image.merge("RGBA", (*rgb.split(), subject_r.split()[-1]))

ox = (TW - nw) // 2
oy = max(8, TH - nh)
canvas.paste(subject_r, (ox, oy), subject_r)

canvas.save(out_home, "PNG", optimize=True)
canvas.save(out_about, "PNG", optimize=True)
print("ok", canvas.size, out_home.stat().st_size)
