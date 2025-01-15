// Animated dog
function drawAnimatedDog() {
  const canvas = document.getElementById("rive-dog");

  if (canvas) {
    const src = canvas.getAttribute("data-src");

    const r = new rive.Rive({
      src: src,
      canvas: canvas,
      autoplay: true,
      stateMachines: "State Machine 1",
      onLoad: () => {
        r.resizeDrawingSurfaceToCanvas();
      },
    });
  }
}

function showSpinner() {
  const spinner = document.getElementById("loading-spinner");
  const popoverMenu = document.getElementById("menu");

  // Show spinner on page unload
  window.addEventListener("beforeunload", function () {
    popoverMenu.hidePopover();
    spinner.classList.remove("d-none");
  });
}

// Messages modal window
function drawModalWindow() {
  const messagesModal = document.getElementById("messagesModal");

  if (messagesModal) {
    const alerts = messagesModal.querySelectorAll(".alert");
    if (alerts.length > 0) {
      const modal = new bootstrap.Modal(messagesModal);

      // Remove `inert` when modal is shown
      messagesModal.addEventListener("shown.bs.modal", function () {
        messagesModal.removeAttribute("inert");
      });

      // Add `inert` when modal is hidden
      messagesModal.addEventListener("hidden.bs.modal", function () {
        messagesModal.setAttribute("inert", "");
      });

      alerts.forEach((alert) => {
        if (alert.classList.contains("success")) {
          alert.innerHTML =
            `<i class="fa-solid fa-xl fa-circle-check text-success me-2"></i>` +
            alert.innerHTML;
        }
        if (alert.classList.contains("danger")) {
          alert.innerHTML =
            `<i class="fa-solid fa-xl fa-circle-exclamation text-danger me-2"></i>` +
            alert.innerHTML;
        }
        if (alert.classList.contains("warning")) {
          alert.innerHTML =
            `<i class="fa-solid fa-xl fa-triangle-exclamation text-warning me-2"></i>` +
            alert.innerHTML;
        }
        if (alert.classList.contains("info")) {
          alert.innerHTML =
            `<i class="fa-solid fa-xl fa-circle-info text-info me-2"></i>` +
            alert.innerHTML;
        }
      });

      modal.show();
    }
  }
}

// Tooltips
function drawTooltip() {
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl);
  });
}

// Show more/less description on event card
function showMoreLessText() {
  document
    .querySelectorAll(".toggle-description")
    .forEach(function (toggleLink) {
      toggleLink.addEventListener("click", function (e) {
        e.preventDefault();
        const eventId = this.getAttribute("data-event-id");
        const truncatedElement = document.getElementById(
          `description-truncated-${eventId}`
        );
        const fullElement = document.getElementById(
          `description-full-${eventId}`
        );

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
}

// Rating
function drawRatingStars() {
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
}

document.addEventListener("DOMContentLoaded", function () {
  drawAnimatedDog();
  showSpinner();
  drawModalWindow();
  drawTooltip();
  showMoreLessText();
  drawRatingStars();
});
