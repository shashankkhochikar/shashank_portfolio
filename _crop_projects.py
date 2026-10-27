"""Crop Upwork screenshot product art into project thumbs (600x389)."""
from PIL import Image
import os
import shutil

base = r"C:\Users\Shashank Khochikar\.cursor\projects\d-PersonalWorkspace-SK-Portfolio-portfolio\assets"
out = r"d:\PersonalWorkspace\SK_Portfolio\portfolio\assets\img"
os.makedirs(out, exist_ok=True)

TARGET = (600, 389)

srcs = {
    "bmi": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-d2589f4d-2fcb-4c2a-95ef-8ac9a2601ee8.png",
    ),
    "openhouses": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-6692bfc4-0dad-4349-a22e-7d62c8f0ab5b.png",
    ),
    "ilaj": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-b542d2e5-804f-4909-b6e1-4ecef7ed91d5.png",
    ),
    "saintfarm": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-c540d82d-53c7-43a7-9aca-f4397e31bc02.png",
    ),
    "essenza": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-eca2cb21-514c-4c69-b7a3-3c875218318b.png",
    ),
    "ezdigital": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-43dec2c3-96e2-46f3-88b1-c67a5010c6fa.png",
    ),
    "probizca": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_image-e0e3a259-f87d-41ec-ad19-3b82871a0e2c.png",
    ),
    "flutter": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_1shared_image__2_-ecf4af38-f0b6-4e59-98d3-25459f9b60e5.jpg",
    ),
    "kotlin": os.path.join(
        base,
        "c__Users_Shashank_Khochikar_AppData_Roaming_Cursor_User_workspaceStorage_fe61aafcd2eb7c83e1097057b6df90d2_images_Gemini_Generated_Image_bsmpt2bsmpt2bsmp-08abb2ed-40f4-4a9c-8e15-413b5e52ee03.jpg",
    ),
}


def fit_cover(im, size=TARGET):
    """Center-crop to aspect ratio then resize (object-fit: cover)."""
    tw, th = size
    target_ratio = tw / th
    w, h = im.size
    ratio = w / h
    if ratio > target_ratio:
        # too wide — crop sides
        nw = int(h * target_ratio)
        left = (w - nw) // 2
        im = im.crop((left, 0, left + nw, h))
    else:
        # too tall — crop top/bottom
        nh = int(w / target_ratio)
        top = (h - nh) // 2
        im = im.crop((0, top, w, top + nh))
    return im.resize(size, Image.LANCZOS)


# Right-side product art crops: (left, top, right, bottom)
crops = {
    "bmi": (580, 95, 990, 490),
    "openhouses": (630, 55, 1005, 495),
    "ilaj": (635, 55, 1005, 505),
    "saintfarm": (630, 55, 1005, 505),
    "essenza": (680, 35, 1024, 480),
    "ezdigital": (605, 45, 1010, 430),
    "probizca": (540, 55, 1010, 505),
}

outputs = {
    "bmi": "projects-1.png",
    "openhouses": "projects-2.png",
    "ilaj": "projects-3.png",
    "saintfarm": "projects-4.png",
    "essenza": "projects-6.png",
    "ezdigital": "projects-7.png",
    "probizca": "projects-8.png",
}

for name, box in crops.items():
    im = Image.open(srcs[name]).convert("RGB")
    c = fit_cover(im.crop(box))
    path = os.path.join(out, outputs[name])
    c.save(path, optimize=True)
    print(path, c.size)

# Voffis uses Flutter logo
flutter = Image.open(srcs["flutter"]).convert("RGB")
fit_cover(flutter).save(os.path.join(out, "projects-5.png"), optimize=True)
print(os.path.join(out, "projects-5.png"), TARGET)
flutter.save(os.path.join(out, "thumb-flutter.jpg"), quality=92, optimize=True)
print("thumb-flutter.jpg", flutter.size)

kotlin = Image.open(srcs["kotlin"]).convert("RGB")
kotlin.save(os.path.join(out, "thumb-kotlin.jpg"), quality=92, optimize=True)
print("thumb-kotlin.jpg", kotlin.size)

preview = os.path.join(out, "_crop_preview")
if os.path.isdir(preview):
    shutil.rmtree(preview)
