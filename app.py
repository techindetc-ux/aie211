import streamlit as st

st.set_page_config(page_title="Smart Autonomous Homestay", layout="wide")

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.main {
    background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
}
.block-container {
    max-width: 1180px;
    padding-top: 95px;
    padding-bottom: 50px;
}
.topbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background: rgba(2, 6, 23, 0.78);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    padding: 10px 28px;
}
.topbar-inner {
    max-width: 1250px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 120px 1fr 120px;
    align-items: center;
}
.apple-left {
    color: white;
    font-size: 20px;
    font-weight: 700;
}
.apple-nav {
    display: flex;
    justify-content: center;
    gap: 30px;
    color: #cbd5e1;
    font-size: 13px;
}
.apple-nav span {
    opacity: 0.92;
}
.apple-right {
    text-align: right;
    color: #cbd5e1;
    font-size: 13px;
}
.hero-text, .card, .cta, .footerbox {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.18);
}
.badge {
    display:inline-block;
    padding:7px 14px;
    border-radius:999px;
    background:#083344;
    color:#a5f3fc;
    font-size:13px;
    margin-bottom:14px;
    border:1px solid rgba(103,232,249,0.15);
}
.h1 {
    font-size: 52px;
    font-weight: 800;
    line-height: 1.12;
    color: white;
    letter-spacing: -0.02em;
}
.h2 {
    font-size: 36px;
    font-weight: 800;
    color: white;
    margin-top: 6px;
    line-height: 1.2;
}
.sub {
    font-size: 18px;
    color: #cbd5e1;
    line-height: 1.8;
}
.section-label {
    color:#67e8f9;
    text-transform:uppercase;
    letter-spacing:2px;
    font-size:13px;
    font-weight:700;
    margin-bottom:10px;
}
.card-title {
    font-size:20px;
    font-weight:700;
    color:white;
}
.small {
    color:#94a3b8;
    font-size:14px;
    line-height:1.7;
}
.metric {
    font-size: 28px;
    font-weight: 800;
    color: #67e8f9;
}
.soft-line {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 46px 0 34px 0;
}
.hero-image-wrap {
    border-radius: 26px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 14px 40px rgba(0,0,0,0.28);
}
.hero-caption {
    color: #94a3b8;
    font-size: 13px;
    margin-top: 10px;
    text-align: center;
}
.stTextInput input, .stTextArea textarea {
    background: #020617 !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    color: white !important;
    border-radius: 16px !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: #64748b !important;
}
.stButton button {
    background: #67e8f9 !important;
    color: #082f49 !important;
    border: none !important;
    border-radius: 16px !important;
    font-weight: 700 !important;
    padding: 0.85rem 1rem !important;
}
img {
    border-radius: 18px;
}
</style>

<div class="topbar">
  <div class="topbar-inner">
    <div class="apple-left">⌂</div>
    <div class="apple-nav">
      <span>Overview</span>
      <span>Problem</span>
      <span>Solution</span>
      <span>Features</span>
      <span>Gallery</span>
      <span>Reviews</span>
      <span>Contact</span>
    </div>
    <div class="apple-right">Smart Stay</div>
  </div>
</div>
""", unsafe_allow_html=True)

pains = [
    "ต้องตอบแชตลูกค้าตลอด 24/7",
    "จัดการการจองหลายช่องทางจนเกิดความผิดพลาดง่าย",
    "กังวลเรื่องผู้เข้าพักเกินจำนวนและความปลอดภัย",
    "ค่าไฟสูงจากการเปิดแอร์หรืออุปกรณ์ทิ้งไว้",
    "งานหลังบ้านเยอะ ทำให้บริหารหลายห้องได้ยาก"
]

features = [
    ("AI Chat 24/7", "ตอบลูกค้าอัตโนมัติ ลดการพลาดโอกาสจอง"),
    ("Booking Automation", "ช่วยจัดการการจองให้เป็นระบบมากขึ้น"),
    ("Security Monitoring", "ช่วยตรวจสอบจำนวนผู้เข้าพักและความปลอดภัย"),
    ("Energy Saving", "ควบคุมพลังงานเพื่อลดต้นทุนค่าไฟ"),
    ("Operation Workflow", "เชื่อมงานทำความสะอาดและหลังเช็กเอาต์"),
    ("Owner Dashboard", "ดูยอดจอง รายได้ และสถานะห้องในที่เดียว")
]

benefits = [
    "เพิ่มโอกาสปิดการจองได้เร็วขึ้น",
    "ลดภาระงานซ้ำ ๆ ของเจ้าของโฮมสเตย์",
    "ควบคุมต้นทุนและเพิ่มกำไรได้ดีขึ้น",
    "บริหารที่พักได้แม้อยู่ไกล",
    "ยกระดับภาพลักษณ์ธุรกิจให้ทันสมัย"
]

faqs = [
    ("เหมาะกับโฮมสเตย์ขนาดเล็กไหม?", "เหมาะ เพราะช่วยลดภาระงานและทำให้บริหารง่ายขึ้น"),
    ("ต้องมีความรู้เทคนิคไหม?", "ไม่จำเป็น ระบบออกแบบให้ใช้งานได้ง่าย"),
    ("ช่วยเรื่องการตลาดไหม?", "ช่วยเพิ่มความเร็วในการตอบลูกค้าและประสบการณ์ก่อนจอง"),
    ("ใช้กับหลายห้องหลายหลังได้ไหม?", "ได้ เหมาะกับผู้ประกอบการที่ต้องการบริหารหลายรายการพร้อมกัน")
]

reviews = [
    ("Nicha Homestay", "ใช้งานแล้วตอบลูกค้าเร็วขึ้นมาก ลดภาระการตอบแชตเองได้จริง", "★★★★★"),
    ("Baan Rim Khao", "ช่วยจัดการการจองได้เป็นระบบขึ้น และดูโปรกว่าการทำเองทั้งหมด", "★★★★★"),
    ("Mekhala Stay", "ชอบตรงที่ช่วยลดงานหลังบ้านและทำให้บริหารหลายห้องง่ายขึ้น", "★★★★★"),
]

gallery_images = [
    "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85",
    "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
    "https://images.unsplash.com/photo-1494526585095-c41746248156",
]

hero_image = "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"

left, right = st.columns([1.1, 1])

with left:
    st.markdown('<div class="hero-text">', unsafe_allow_html=True)
    st.markdown('<div class="badge">SMART AUTONOMOUS HOMESTAY / NEXT</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="h1">เปลี่ยนโฮมสเตย์ธรรมดา<br><span style="color:#67e8f9;">ให้บริหารได้อัตโนมัติด้วย AI</span></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="sub">ระบบสำหรับเจ้าของโฮมสเตย์ที่ต้องการลดภาระงาน เพิ่มความเร็วในการตอบลูกค้า ควบคุมการจอง ความปลอดภัย และต้นทุนในระบบเดียว</p>',
        unsafe_allow_html=True
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><div class="metric">24/7</div><div class="small">ตอบลูกค้าอัตโนมัติ</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><div class="metric">All-in-One</div><div class="small">รวมงานสำคัญไว้ระบบเดียว</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card"><div class="metric">Smart Cost</div><div class="small">ช่วยควบคุมต้นทุนพลังงาน</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="hero-image-wrap">', unsafe_allow_html=True)
    st.image(hero_image, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-caption">Smart homestay experience designed for modern owners</div>', unsafe_allow_html=True)

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Problem</div>', unsafe_allow_html=True)
st.markdown('<div class="h2">ธุรกิจโฮมสเตย์เติบโตยาก เมื่อทุกอย่างยังต้องทำเองทั้งหมด</div>', unsafe_allow_html=True)
st.markdown('<p class="sub">ทั้งการตอบแชต การจอง การควบคุมต้นทุน และการจัดการหลังบ้าน ล้วนใช้เวลาและทำให้เสียโอกาสทางธุรกิจได้ง่าย</p>', unsafe_allow_html=True)

cols = st.columns(3)
for i, pain in enumerate(pains):
    with cols[i % 3]:
        st.markdown(f'<div class="card">{pain}</div>', unsafe_allow_html=True)

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
a, b = st.columns([1.1, 1])

with a:
    st.markdown('<div class="section-label">Solution</div>', unsafe_allow_html=True)
    st.markdown('<div class="h2">AI และ Automation ที่ออกแบบมาเพื่อเจ้าของโฮมสเตย์</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub">ช่วยให้การตอบลูกค้า การจอง การรักษาความปลอดภัย และการควบคุมพลังงานเป็นระบบมากขึ้น โดยยังคงประสบการณ์ที่ดีให้ผู้เข้าพัก</p>', unsafe_allow_html=True)

with b:
    st.markdown('<div class="card"><div class="card-title">สิ่งที่คุณจะได้</div></div>', unsafe_allow_html=True)
    for item in benefits:
        st.markdown(f'<div class="card" style="margin-top:10px;">{item}</div>', unsafe_allow_html=True)

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Features</div>', unsafe_allow_html=True)
st.markdown('<div class="h2">ฟีเจอร์สำคัญที่ช่วยให้บริหารง่ายขึ้นในหน้าเดียว</div>', unsafe_allow_html=True)

fcols = st.columns(3)
for i, (title, desc) in enumerate(features):
    with fcols[i % 3]:
        st.markdown(
            f'<div class="card"><div class="card-title">{title}</div><div class="small" style="margin-top:10px;">{desc}</div></div>',
            unsafe_allow_html=True
        )

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Gallery</div>', unsafe_allow_html=True)
st.markdown('<div class="h2">ตัวอย่างบรรยากาศโฮมสเตย์</div>', unsafe_allow_html=True)

gcols = st.columns(3)
for i, img in enumerate(gallery_images):
    with gcols[i % 3]:
        st.image(img, use_container_width=True)

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Reviews</div>', unsafe_allow_html=True)
st.markdown('<div class="h2">เสียงตอบรับจากผู้ใช้งาน</div>', unsafe_allow_html=True)

rcols = st.columns(3)
for i, (name, text, stars) in enumerate(reviews):
    with rcols[i % 3]:
        st.markdown(
            f'''
            <div class="card">
                <div class="card-title">{name}</div>
                <div style="color:#facc15;font-size:22px;margin:8px 0;">{stars}</div>
                <div class="small">{text}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
st.markdown('<div class="section-label">FAQ</div>', unsafe_allow_html=True)
st.markdown('<div class="h2">คำถามก่อนตัดสินใจ</div>', unsafe_allow_html=True)

for q, ans in faqs:
    st.markdown(
        f'<div class="card" style="margin-top:12px;"><div class="card-title">{q}</div><div class="small" style="margin-top:10px;">{ans}</div></div>',
        unsafe_allow_html=True
    )

st.markdown("<hr class='soft-line'>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Contact</div>', unsafe_allow_html=True)
st.markdown('<div class="cta">', unsafe_allow_html=True)
st.markdown('<div class="h2">พร้อมยกระดับโฮมสเตย์ของคุณแล้วหรือยัง?</div>', unsafe_allow_html=True)
st.markdown('<p class="sub">เริ่มต้นด้วยการขอเดโม เพื่อดูว่าระบบนี้ช่วยลดภาระงานและเพิ่มประสิทธิภาพให้ธุรกิจของคุณได้อย่างไร</p>', unsafe_allow_html=True)

name = st.text_input("ชื่อผู้ติดต่อ")
contact = st.text_input("เบอร์โทร / อีเมล")
business = st.text_input("ชื่อโฮมสเตย์หรือธุรกิจของคุณ")
problem = st.text_area("ปัญหาที่คุณอยากให้ระบบช่วยแก้")

if st.button("ส่งข้อมูลเพื่อขอเดโม", use_container_width=True):
    st.success("ส่งข้อมูลเรียบร้อยแล้ว")
    st.write({
        "name": name,
        "contact": contact,
        "business": business,
        "problem": problem
    })

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footerbox" style="margin-top:40px;">
  <div class="section-label">Smart Autonomous Homestay / Next</div>
  <div class="small">AI + Automation เพื่อช่วยให้เจ้าของโฮมสเตย์บริหารง่ายขึ้น ขายดีขึ้น และเติบโตอย่างเป็นระบบ</div>
</div>
""", unsafe_allow_html=True)