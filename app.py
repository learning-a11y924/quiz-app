import streamlit as st

# ==========================================
# سوالات آزمون
# ==========================================

questions = [{'question': 'بر اساس این سند، کارکرد اصلی فرماندهی آشتار چیست؟', 'options': ['مدیریت بازسازی نظام مالی جدید پس از رویداد', 'ایفای نقش به عنوان نیروی مداخله\u200cگر برای آزادسازی سیاره زمین از چنگال نیروهای تاریک', 'برقراری نخستین تماس رسمی با دولت\u200cهای سطح زمین', 'نظارت بر عملیات «جنبش مقاومت» از مدار زمین'], 'answer': 1}, {'question': 'بر اساس توصیف ارائه\u200cشده توسط پلِیادی\u200cها، تفاوت سیاره ایکس با تهدیدی که اغلب به نیبیرو نسبت داده می\u200cشود، چیست؟', 'options': ['مدار آن پایدار است و هرگز به فاصله\u200cای کمتر از فاصله پلوتو تا زمین، به زمین نزدیک نمی\u200cشود', 'این سیاره میزبان شبکه گسترده\u200cای از پایگاه\u200cهای زیرزمینی است که توسط نیروهای نور اداره می\u200cشوند', 'جرم آن ۰٫۷۶ برابر جرم زمین است که برای ایجاد اختلال در سایر سیارات کافی نیست', 'سطح آن با یخ متان پوشیده شده و به همین دلیل ته\u200cرنگی متمایل به آبی دارد'], 'answer': 0}, {'question': 'هدف از وجود ایمپلنت\u200cهایی که طبق توضیحات متن در لوب پیشانی مغز قرار دارند، چیست؟', 'options': ['از بین بردن انرژی جنسی و کندالینی', 'فعال\u200cسازی برنامه\u200cهای کنترل ذهن از نوع ام\u200cکی-اولترا از راه دور', 'گرفتار نگه داشتن فرد در ترس\u200cهای مربوط به بقا', 'مختل کردن فرآیند تصمیم\u200cگیری و جدا نگه داشتن فرد از «منبع» '], 'answer': 3}, {'question': 'بر اساس این سند، دلیل اصلی ترویج واکسیناسیون اجباری توسط نیروهای تاریک چیست؟', 'options': ['گسترش بیماری\u200cها و کاهش جمعیت جهان', 'وارد کردن بیوچیپ\u200cهای فیزیکی به منظور تقویت برنامه\u200cهای کنترلی', 'آزمودن میزان فرمان\u200cبرداری جمعیت ساکن سطح زمین در برابر «نظم نوین جهانی', ' کسب سودهای کلان برای شرکت\u200cهای بزرگ داروسازی'], 'answer': 1}, {'question': 'نقش گروه\u200cهای خواهران رز  که به تشکیل آن\u200cها تشویق می\u200cشود، چیست؟', 'options': ['ایجاد جزایر نور فیزیکی و جوامع خودکفا', 'انجام اقدامات نافرمانی مدنی برای افشای کابال', 'مذاکره مستقیم برای تسلیم شدن اعضای رده \u200cپایین کابال', 'تثبیت و لنگر انداختن انرژی\u200cهای الهه در شبکه انرژی سیاره\u200cای'], 'answer': 3}, {'question': 'بر اساس متن، پایگاه جنبش مقاومت کجاست؟', 'options': ['در شهرهای زیرزمینی واقع در بخش بالایی پوسته زمین', 'به \u200cصورت نفوذ یافته در میان دولت\u200cها و ارتش\u200cهای جمعیت ساکن سطح زمین', 'در پایگاه\u200cهای مخفی در قطب جنوب، هم\u200cمکان با گروه کیمرا', 'در سفینه\u200cهای مادر ناوگان پلدین ها در مدار زمین'], 'answer': 0}, {'question': 'در جریان تهاجم آرکان\u200cها در سال ۱۹۹۶، کدام نژاد بیگانه که پیش\u200cتر صلح\u200cجو بود، مورد حمله قرار گرفت و شماری از اعضایش در پایگاه\u200cهای زیرزمینی روی زمین به گروگان گرفته شدند؟', 'options': ['پلدین ها', 'آندرومدایی\u200cها ', 'سیرین\u200cها ', 'آرکتوریان\u200cها '], 'answer': 0}, {'question': 'بر اساس متون کبرا، کارکرد اصلی جنبش مقاومت چیست؟', 'options': ['ساخت سفینه\u200cهای مادر در مدار زمین برای آمادگی جهت اولین تماس', 'حفظ یک قرنطینه انرژی در اطراف زمین برای محافظت از بشریت', 'زندگی در سکونتگاه\u200cهای زیرزمینی و حمایت از نیروهای نظامی مثبت برای متوقف کردن کابال', 'برقراری تماس مستقیم با رهبران جهان برای مذاکره جهت گذاری مسالمت\u200cآمیز'], 'answer': 2}, {'question': 'بر اساس متون، دلیل واقعی آتش\u200cسوزی کلیسای نوتردام پاریس در آوریل ۲۰۱۹ چه بود؟', 'options': ['یک عملیات پرچم دروغین برای متحد کردن مردم فرانسه در اندوه و سوگواری', 'اقدامی از سوی نیروهای نور برای پاکسازی یک مکان باستانیِ قربانی\u200cکردن', 'تلاشی از سوی کابال برای نابودی یک گرداب انرژیِ الهه ', 'حادثه\u200cای ناشی از عملیات نوسازی با نظارت نامناسب'], 'answer': 2}, {'question': 'بر اساس توضیحات موجود در سند، سنگ\u200cهای سینتامانی  چه هستند؟', 'options': ['ابزارهای ارتباطی که توسط جنبش مقاومت ساخته شده\u200cاند', 'کریستال\u200cهایی از تمدن لموریا که برای ذخیره\u200cسازی اطلاعات باستانی به کار می\u200cرفته\u200cاند', 'قطعاتی از سیاره\u200cای در منظومه ستاره\u200cای سیروس - شباهنگ که منفجر شده است', 'سنگ\u200cهایی که توسط کنت سنت ژرمن برای تأمین مالی پروژه\u200cهای مادی خلق شده\u200cاند'], 'answer': 2}]

# ==========================================
# تنظیمات صفحه
# ==========================================

st.set_page_config(
    page_title="آزمون",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==========================================
# ظاهر برنامه
# ==========================================

st.markdown(
    """
    <style>
    /* زمینه کاملاً مشکی */
    .stApp {
        background: #000000;
    }

    /* متن‌های عمومی */
    .stApp, .stMarkdown, p, label, div {
        color: #ffffff;
    }

    /* عنوان */
    .quiz-title {
        color: #a855f7;
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin: 20px 0 12px 0;
    }

    /* اطلاعات بالای آزمون */
    .quiz-info {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
        margin: 12px 0 20px 0;
        direction: rtl;
    }

    /* متن سؤال */
    .question-text {
        color: #ffffff;
        text-align: center;
        font-size: 25px;
        font-weight: 700;
        line-height: 1.9;
        margin: 10px 0 26px 0;
        direction: rtl;
    }

    /* نوار پیشرفت */
    div[data-testid="stProgress"] > div > div {
        background-color: #a855f7;
    }

    /* رادیوها: بدون جعبه و با متن سفید */
    div[data-testid="stRadio"] {
        direction: rtl;
    }

    div[data-testid="stRadio"] > label {
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: 500 !important;
        margin-bottom: 8px;
    }

    div[data-testid="stRadio"] [role="radiogroup"] {
        gap: 10px;
    }

    div[data-testid="stRadio"] [role="radio"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #ffffff !important;
        padding: 5px 0 !important;
    }

    div[data-testid="stRadio"] [role="radio"] p {
        color: #ffffff !important;
        font-size: 20px !important;
        margin: 0 !important;
    }

    /* دایره انتخاب */
    div[data-testid="stRadio"] [role="radio"] > div:first-child {
        background: transparent !important;
        border-color: #ffffff !important;
    }

    /* حالت انتخاب‌شده */
    div[data-testid="stRadio"] [role="radio"][aria-checked="true"] > div:first-child {
        border-color: #a855f7 !important;
        background-color: #a855f7 !important;
    }

    /* دکمه‌ها */
    div.stButton > button {
        background: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #a855f7 !important;
        border-radius: 10px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
    }

    div.stButton > button:hover {
        border-color: #c084fc !important;
        color: #ffffff !important;
    }

    /* پیام‌ها */
    div[data-testid="stAlert"] {
        direction: rtl;
    }

    /* نتیجه نهایی */
    .final-result {
        color: #ffffff;
        text-align: center;
        background: #0a0a0a;
        border: 1px solid #333333;
        border-radius: 14px;
        padding: 22px;
        line-height: 2.2;
        font-size: 20px;
        direction: rtl;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# وضعیت هر کاربر
# ==========================================

defaults = {
    "current_question": 0,
    "score": 0,
    "solved": False,
    "had_wrong_answer": False,
    "wrong_options": [],
    "result_message": "",
    "finished": False,
    "selected_answer": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def reset_current_question():
    st.session_state.solved = False
    st.session_state.had_wrong_answer = False
    st.session_state.wrong_options = []
    st.session_state.result_message = ""
    st.session_state.selected_answer = None


def check_answer():
    selected = st.session_state.selected_answer

    if selected is None or st.session_state.solved:
        return

    correct = questions[st.session_state.current_question]["answer"]

    if selected == correct:
        st.session_state.solved = True

        if not st.session_state.had_wrong_answer:
            st.session_state.score += 1

        if st.session_state.had_wrong_answer:
            st.session_state.result_message = "success:✅ آفرین! گزینه صحیح را پیدا کردی"
        else:
            st.session_state.result_message = "success:✅ پاسخ شما صحیح است"

    else:
        st.session_state.had_wrong_answer = True

        if selected not in st.session_state.wrong_options:
            st.session_state.wrong_options.append(selected)

        st.session_state.result_message = (
            f"error:❌ پاسخ غلط است | جواب صحیح: گزینه {correct + 1} | "
            "گزینه صحیح را انتخاب کن"
        )


def next_question():
    st.session_state.current_question += 1
    reset_current_question()


def restart_quiz():
    for key, value in defaults.items():
        st.session_state[key] = value
    st.rerun()


# ==========================================
# نتیجه نهایی
# ==========================================

if st.session_state.finished:
    total = len(questions)
    score = st.session_state.score
    wrong = total - score
    percentage = (score / total) * 100

    st.markdown(
        '<div class="quiz-title">🎉 آزمون تمام شد!</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="final-result">
            تعداد سوالات: <strong>{total}</strong><br>
            پاسخ صحیح: <strong>{score}</strong><br>
            پاسخ غلط: <strong>{wrong}</strong><br>
            درصد: <strong>{percentage:.1f}%</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if st.button("🔄 شروع دوباره آزمون", use_container_width=True):
        restart_quiz()

    st.stop()

# ==========================================
# سؤال جاری
# ==========================================

index = st.session_state.current_question
data = questions[index]
total = len(questions)

st.markdown('<div class="quiz-title">آزمون</div>', unsafe_allow_html=True)

st.progress(
    (index + 1) / total,
    text=f"سوال {index + 1} از {total}"
)

st.markdown(
    f"""
    <div class="quiz-info">
        <span>امتیاز: {st.session_state.score}</span>
        <span>سوال {index + 1} از {total}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="question-text">{data["question"]}</div>',
    unsafe_allow_html=True,
)

# ==========================================
# گزینه‌ها - رادیویی و بدون جعبه
# ==========================================

disabled_options = set(st.session_state.wrong_options)

available_options = [
    (i, option)
    for i, option in enumerate(data["options"])
    if i not in disabled_options
]

options_text = [f"{i + 1}) {option}" for i, option in available_options]

if st.session_state.solved:
    selected_index = None
    st.radio(
        "گزینه‌ها",
        options_text,
        index=None,
        disabled=True,
        label_visibility="collapsed",
        key=f"answered_{index}",
    )
else:
    # بعد از پاسخ غلط، گزینه‌های اشتباه قبلی از انتخاب‌های قابل‌انتخاب حذف می‌شوند.
    selected_pos = st.radio(
        "گزینه‌ها",
        options_text,
        index=None,
        disabled=False,
        label_visibility="collapsed",
        key=f"radio_{index}_{len(disabled_options)}",
    )

    if selected_pos is not None:
        selected_actual_index = available_options[options_text.index(selected_pos)][0]
        st.session_state.selected_answer = selected_actual_index

# ==========================================
# ثبت پاسخ
# ==========================================

if not st.session_state.solved:
    if st.button("✓ ثبت پاسخ", use_container_width=True):
        if st.session_state.selected_answer is None:
            st.warning("لطفاً یکی از گزینه‌ها را انتخاب کن.")
        else:
            check_answer()
            st.rerun()

# ==========================================
# پیام پاسخ
# ==========================================

if st.session_state.result_message:
    msg_type, msg = st.session_state.result_message.split(":", 1)

    if msg_type == "success":
        st.success(msg)
    else:
        st.error(msg)

# ==========================================
# سؤال بعدی
# ==========================================

if st.session_state.solved:
    st.write("")
    if index + 1 < total:
        if st.button("➡️ سوال بعدی", use_container_width=True):
            next_question()
            st.rerun()
    else:
        if st.button("🏁 مشاهده نتیجه نهایی", use_container_width=True):
            st.session_state.finished = True
            st.rerun()
