function typeWriterEffect(elementId, textArray, typingSpeed = 100, pauseTime = 1000) {
    let i = 0;
    let j = 0;
    let isDeleting = false;
    const target = document.getElementById(elementId);
  
    function type() {
      const current = textArray[i];
      target.textContent = isDeleting
        ? current.substring(0, j--)
        : current.substring(0, j++);
  
      if (!isDeleting && j === current.length) {
        isDeleting = true;
        setTimeout(type, pauseTime);
      } else if (isDeleting && j === 0) {
        isDeleting = false;
        i = (i + 1) % textArray.length;
        setTimeout(type, 200);
      } else {
        setTimeout(type, isDeleting ? 50 : typingSpeed);
      }
    }
    type();
  }
  
  typeWriterEffect("typewriter-home", ["Data Analytics💻", "Creative Thinker 🎨"]);
  typeWriterEffect("typewriter-about", ["🎓 BSCS (Bachelor of Science in Computer Science)",  "📱 Mobile App Developer – XML | Java | Android",
    "💡 AI & ML Explorer – Python | Sklearn | Data Analysis",
    "🌐 Web Scraping Enthusiast – Python | Selenium | BeautifulSoup",
    "🌱 Currently learning MLKit"]);
  
  const projectCards = document.querySelectorAll('.project-card');
  function animateCardsOnScroll() {
    projectCards.forEach(card => {
      const rect = card.getBoundingClientRect();
      if (rect.top < window.innerHeight - 50) {
        card.classList.add('visible');
      }
    });
  }
  window.addEventListener('scroll', animateCardsOnScroll);
  window.addEventListener('load', animateCardsOnScroll);
  document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Thank you for reaching out! I will get back to you soon.');
    this.reset();
  });
  document.querySelectorAll('.circular-skill').forEach(el => {
    const percent = el.getAttribute('data-percent');
    const degrees = (percent / 100) * 360;
    el.querySelector('.circle').style.setProperty('--progress', degrees + 'deg');
  })
  const toggleBtn = document.getElementById('theme-toggle');
  const icon = toggleBtn.querySelector('i');

    // Load saved theme
    if (localStorage.getItem('theme') === 'dark') {
      document.body.classList.add('dark-mode');
      icon.classList.replace('fa-moon', 'fa-sun');
    }
  
    toggleBtn.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      const isDark = document.body.classList.contains('dark-mode');
      icon.classList.toggle('fa-moon', !isDark);
      icon.classList.toggle('fa-sun', isDark);
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
 const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.getElementById('nav-links');

  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
