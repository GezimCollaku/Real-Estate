document.addEventListener('DOMContentLoaded', () => {
  const points = document.querySelectorAll('.key-points .card');

  function revealPoints() {
    const windowHeight = window.innerHeight;
    points.forEach((point) => {
      const pointTop = point.getBoundingClientRect().top;
      if(pointTop < windowHeight - 100) {
        point.classList.add('show');
      }
    });
  }

  window.addEventListener('scroll', revealPoints);
  window.addEventListener('resize', revealPoints);
  revealPoints(); // për rastin kur disa janë fillimisht në view
});


const track = document.querySelector('.slider-track');
track.innerHTML += track.innerHTML;