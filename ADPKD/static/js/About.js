document.addEventListener("DOMContentLoaded", function () {
    let imgBoxes = document.querySelectorAll('.img-box');
    let teamContents = document.querySelectorAll('.team-content');
    let memberBios = document.querySelectorAll('.memberBx');
	let img = document.querySelectorAll('.img-box img');

    // Ensure first member is visible on page load
    teamContents.forEach((content, i) => {
        content.style.display = i === 0 ? 'block' : 'none';
    });
    memberBios.forEach((bio, i) => {
        bio.style.display = i === 0 ? 'block' : 'none';
    });
    imgBoxes.forEach((box, index) => {
        box.addEventListener('mouseover', function () {
            let targetIdDetails = this.getAttribute("data-id"); // e.g., "member-content-details-1"
            let targetIdBio = targetIdDetails.replace("details", "bio");

            // Highlight selected image
            imgBoxes.forEach((b, i) => {
                b.style.boxShadow = i === index
                    ? "0 0 0 2px #222222, 0 0 0 6px #ff1d50"
                    : "0 0 0 2px #222222, 0 0 0 4px rgb(255, 255, 255)";
            });

	//Icon image color change
	img.forEach((im, i) => {
                im.style.filter = i === index
                    ? "grayscale(0)"
                    : "grayscale(1)";
            });

            // Show related team-content
            teamContents.forEach(content => {
                content.style.display = content.id === targetIdDetails ? 'block' : 'none';
            });

            // Show related member bio
            memberBios.forEach(bio => {
                bio.style.display = bio.id === targetIdBio ? 'block' : 'none';
            });
        });
    });
});