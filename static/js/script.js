// Tooltips
document.addEventListener("DOMContentLoaded", function () {
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
});

// Show more/less on event card
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".toggle-content").forEach(function (toggleLink) {
    toggleLink.addEventListener("click", function (e) {
      e.preventDefault();
      const eventId = this.getAttribute("data-event-id");
      const truncatedElement = document.getElementById(
        `content-truncated-${eventId}`
      );
      const fullElement = document.getElementById(`content-full-${eventId}`);

      if (truncatedElement.classList.contains("d-none")) {
        truncatedElement.classList.remove("d-none");
        fullElement.classList.add("d-none");
        this.textContent = "Show More";
      } else {
        truncatedElement.classList.add("d-none");
        fullElement.classList.remove("d-none");
        this.textContent = "Show Less";
      }
    });
  });
});

// Rating
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
