const r = new rive.Rive({
  src: doggoAnimationURL,
  canvas: document.getElementById("rive-dog"),
  autoplay: true,
  stateMachines: "State Machine 1",
  onLoad: () => {
    r.resizeDrawingSurfaceToCanvas();
  },
});

document.addEventListener("DOMContentLoaded", function () {
  const stars = document.querySelectorAll(".star-btn");
  const ratingInput = document.getElementById("rating-value");

  stars.forEach((star) => {
    star.addEventListener("click", function () {
      const rating = this.getAttribute("data-value");
      ratingInput.value = rating;

      stars.forEach((s) => {
        const starValue = s.getAttribute("data-value");
        const starIcon = s.querySelector("i");

        if (starValue <= rating) {
          starIcon.classList.add("fa-solid");
          starIcon.classList.remove("fa-regular");
        } else {
          starIcon.classList.add("fa-regular");
          starIcon.classList.remove("fa-solid");
        }
      });
    });
  });
});

document.addEventListener("DOMContentLoaded", function () {
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
});
