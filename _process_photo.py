from pathlib import Path
from PIL import Image, ImageEnhance
from rembg import remove

src = Path(
    r"C:\Users\Shashank Khochikar\.cursor\projects\d-PersonalWorkspace-SK-Portfolio-portfolio\assets"
    r"\c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_"
    r"fe61aafcd2eb7c83e1097057b6df90d2_images_Professional_Corporate_Headshot__2_"
    r"-99daae58-d3e4-4ab1-9d28-78ed794ad5f7.jpg"
)
out_dir = Path(r"d:\PersonalWorkspace\SK_Portfolio\portfolio\assets\img")
out_home = out_dir / "home-perfil.png"
out_about = out_dir / "about-perfil.png"
backup = out_dir / "home-perfil-original-backup.png"

if out_home.exists() and not backup.exists():
    Image.open(out_home).save(backup)

img = Image.open(src).convert("RGBA")
print("source", img.size)

cutout = remove(img).convert("RGBA")
alpha = cutout.split()[-1]
bbox = alpha.getbbox()
print("bbox", bbox)

pad = 40
x0, y0, x1, y1 = bbox
x0 = max(0, x0 - pad)
y0 = max(0, y0 - pad)
x1 = min(cutout.width, x1 + pad)
y1 = min(cutout.height, y1 + pad)
subject = cutout.crop((x0, y0, x1, y1))
print("subject", subject.size)

TW, TH = 800, 937
canvas = Image.new("RGBA", (TW, TH), (0, 0, 0, 255))

sw, sh = subject.size
scale = min((TW * 0.92) / sw, (TH * 0.96) / sh)
nw, nh = int(sw * scale), int(sh * scale)
subject_r = subject.resize((nw, nh), Image.Resampling.LANCZOS)

subject_rgb = subject_r.convert("RGB")
subject_rgb = ImageEnhance.Contrast(subject_rgb).enhance(1.05)
subject_rgb = ImageEnhance.Color(subject_rgb).enhance(1.05)
subject_r = Image.merge("RGBA", (*subject_rgb.split(), subject_r.split()[-1]))

ox = (TW - nw) // 2
oy = max(10, TH - nh)
canvas.paste(subject_r, (ox, oy), subject_r)

canvas.save(out_home, "PNG", optimize=True)
canvas.save(out_about, "PNG", optimize=True)
print("saved", out_home, out_home.stat().st_size)
print("saved", out_about, out_about.stat().st_size)
print("final", canvas.size, canvas.mode)
