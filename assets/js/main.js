/*=============== HOME TAGLINES SLIDER ===============*/
const taglinesRoot = document.querySelector(".home__taglines");
const taglinesTrack = document.querySelector(".home__taglines-track");
const taglines = document.querySelectorAll(".home__tagline");

if (taglinesRoot && taglinesTrack && taglines.length > 1) {
  let taglineIndex = 0;
  const TAGLINE_INTERVAL = 4000;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const slideTagline = () => {
    taglineIndex = (taglineIndex + 1) % taglines.length;
    const offset = taglines[taglineIndex].offsetTop;
    taglinesTrack.style.transform = `translateY(-${offset}px)`;
  };

  if (!reduceMotion) {
    setInterval(slideTagline, TAGLINE_INTERVAL);
  }
}

/*=============== WORK TABS ===============*/
const tabs = document.querySelectorAll("[data-target]");
const tabContents = document.querySelectorAll("[data-content]");

const showWorkPanel = (panel) => {
  if (!panel) return;

  tabContents.forEach((content) => content.classList.remove("work-active"));
  panel.classList.add("work-active");

  /* ScrollReveal can leave opacity:0 on cards that were display:none */
  panel.querySelectorAll(".work__card").forEach((card) => {
    card.style.opacity = "1";
    card.style.visibility = "visible";
    card.style.transform = "none";
  });
};

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    const target = document.querySelector(tab.dataset.target);

    showWorkPanel(target);

    tabs.forEach((item) => item.classList.remove("work-active"));
    tab.classList.add("work-active");
  });
});

/*=============== SERVICES ACCORDION ===============*/
const accordionItems = document.querySelectorAll(".services__card");

const toggleItem = (item) => {
  const accordionContent = item.querySelector(".services__info");

  if (item.classList.contains("accordion-open")) {
    accordionContent.removeAttribute("style");
    item.classList.remove("accordion-open");
  } else {
    accordionContent.style.height = accordionContent.scrollHeight + "px";
    item.classList.add("accordion-open");
  }
};

accordionItems.forEach((item) => {
  const accordionHeader = item.querySelector(".services__header");

  accordionHeader.addEventListener("click", () => {
    const openItem = document.querySelector(".accordion-open");

    toggleItem(item);

    if (openItem && openItem !== item) {
      toggleItem(openItem);
    }
  });
});

const openService = document.querySelector(".services__card.accordion-open .services__info");
if (openService) {
  openService.style.height = openService.scrollHeight + "px";
}

/*=============== COPY EMAIL IN CONTACT ===============*/
const copyBtn = document.getElementById("contact-button");
const contactEmail = document.querySelector(".contact__email");

if (copyBtn && contactEmail) {
  const originalHtml = copyBtn.innerHTML;
  const email = contactEmail.textContent.trim();

  const copyEmail = async () => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(email);
      return;
    }

    const input = document.createElement("textarea");
    input.value = email;
    input.setAttribute("readonly", "");
    input.style.position = "absolute";
    input.style.left = "-9999px";
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    document.body.removeChild(input);
  };

  copyBtn.addEventListener("click", async () => {
    try {
      await copyEmail();
      copyBtn.innerHTML = 'Email copied <i class="ri-check-line"></i>';
    } catch (error) {
      copyBtn.innerHTML = 'Email copied <i class="ri-check-line"></i>';
    }

    setTimeout(() => {
      copyBtn.innerHTML = originalHtml;
    }, 2000);
  });
}

/*=============== CURRENT YEAR OF THE FOOTER ===============*/
const footerYear = document.getElementById("footer-year");

if (footerYear) {
  footerYear.textContent = new Date().getFullYear();
}

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll("section[id]");

const scrollActive = () => {
  const scrollDown = window.scrollY;

  sections.forEach((current) => {
    const sectionHeight = current.offsetHeight;
    const sectionTop = current.offsetTop - 58;
    const sectionId = current.getAttribute("id");
    const sectionsClass = document.querySelector(".nav__menu a[href*=" + sectionId + "]");

    if (!sectionsClass) return;

    if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
      sectionsClass.classList.add("active-link");
    } else {
      sectionsClass.classList.remove("active-link");
    }
  });
};

window.addEventListener("scroll", scrollActive);

/*=============== HEADER BACKGROUND ON SCROLL ===============*/
const header = document.getElementById("header");

const scrollHeader = () => {
  if (!header) return;

  if (window.scrollY >= 40) {
    header.classList.add("scroll-header");
  } else {
    header.classList.remove("scroll-header");
  }
};

window.addEventListener("scroll", scrollHeader);
scrollHeader();

/*=============== CUSTOM CURSOR ===============*/
const cursor = document.getElementById("cursor");

if (cursor && window.matchMedia("(min-width: 1151px) and (hover: hover)").matches) {
  window.addEventListener("mousemove", (event) => {
    cursor.style.left = event.clientX + "px";
    cursor.style.top = event.clientY + "px";
    cursor.classList.remove("cursor--hidden");
  });

  document.addEventListener("mouseleave", () => {
    cursor.classList.add("cursor--hidden");
  });

  /* Hide custom cursor on links */
  const hoverTargets = document.querySelectorAll("a, button");

  hoverTargets.forEach((target) => {
    target.addEventListener("mouseenter", () => cursor.classList.add("cursor--hover"));
    target.addEventListener("mouseleave", () => cursor.classList.remove("cursor--hover"));
  });
}

/*=============== PROJECTS CARD TILT ===============*/
const projectCards = document.querySelectorAll(".projects__card");
const tiltQuery = window.matchMedia("(min-width: 768px) and (hover: hover)");
const reduceMotionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
const TILT_MAX = 45;

const resetTilt = (card) => {
  card.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg)";
};

const onCardMove = (event) => {
  const card = event.currentTarget;
  const rect = card.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  const rotateY = ((x / rect.width) - 0.5) * (TILT_MAX * 2);
  const rotateX = ((y / rect.height) - 0.5) * -(TILT_MAX * 2);

  card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg)`;
};

const onCardLeave = (event) => {
  resetTilt(event.currentTarget);
};

const bindProjectTilt = () => {
  const enable = tiltQuery.matches && !reduceMotionQuery.matches;

  projectCards.forEach((card) => {
    card.removeEventListener("mousemove", onCardMove);
    card.removeEventListener("mouseleave", onCardLeave);
    resetTilt(card);

    if (enable) {
      card.addEventListener("mousemove", onCardMove);
      card.addEventListener("mouseleave", onCardLeave);
    }
  });
};

if (projectCards.length) {
  bindProjectTilt();
  tiltQuery.addEventListener("change", bindProjectTilt);
  reduceMotionQuery.addEventListener("change", bindProjectTilt);
}

/*=============== SCROLL REVEAL ANIMATION ===============*/
const prefersReducedMotion = reduceMotionQuery.matches;

if (!prefersReducedMotion && typeof ScrollReveal !== "undefined") {
  const sr = ScrollReveal({
    origin: "top",
    distance: "28px",
    duration: 800,
    delay: 80,
    easing: "cubic-bezier(.22, 1, .36, 1)",
    viewFactor: 0.12,
  });

  sr.reveal(".section__title");
  sr.reveal(".home__data", { origin: "left", delay: 120 });
  sr.reveal(".home__info", { origin: "right", delay: 180 });
  sr.reveal(".home__perfil", { delay: 280, scale: 0.96 });
  sr.reveal(".about__perfil", { origin: "left" });
  sr.reveal(".about__info", { origin: "right" });
  sr.reveal(".projects__card", { origin: "bottom", interval: 90 });
  sr.reveal(".work__filters", { distance: "16px" });
  sr.reveal(".work__content.work-active .work__card", { origin: "bottom", interval: 80 });
  sr.reveal(".services__card", { origin: "bottom", interval: 100 });
  sr.reveal(".testimonials__card", { origin: "bottom", interval: 80 });
  sr.reveal(".contact__data", { origin: "left" });
  sr.reveal(".contact__info", { origin: "right" });
}
