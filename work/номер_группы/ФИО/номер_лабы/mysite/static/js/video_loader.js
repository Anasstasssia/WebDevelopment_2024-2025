document.addEventListener("DOMContentLoaded", function () {
    const videoData = {
        bombardino_crocodilo: [
            "/static/video/IMG_7530.mp4",
            "/static/video/IMG_7631.mp4",
            "/static/video/IMG_7553.mp4",
        ],
        brr_brr_patapin: [
            "/static/video/IMG_7530.mp4",
            "/static/video/IMG_7631.mp4",
            "/static/video/IMG_7553.mp4",
        ],
        tralalero_tralala: [
            "/static/video/IMG_7495.mp4",
            "/static/video/IMG_7627.mp4",
            "/static/video/IMG_7546.mp4",
            "/static/video/IMG_7529.mp4",

        ],

        tung_tung_tung_sahur: [
            "/static/video/IMG_7496.mp4",
            "/static/video/IMG_7578.mp4",
            "/static/video/IMG_7693.mp4",
        ],

        chimpanzini_bananini: [
            "/static/video/IMG_7659.mp4",
        ],

        another_meme: [
            "/static/video/IMG_7495.mp4",
            "/static/video/IMG_7627.mp4",
            "/static/video/IMG_7546.mp4",
            "/static/video/IMG_7529.mp4",

        ],

    };

    const gridClasses = {
        bombardino_crocodilo: "video-grid",
        brr_brr_patapin: "video-grid",
        tralalero_tralala: "video-grid",
        tung_tung_tung_sahur: "video-grid",
        chimpanzini_bananini: "video-grid",
        another_meme: "video-grid",
    };

    for (const [key, videos] of Object.entries(videoData)) {
        const container = document.getElementById(`container-${key}`);
        if (!container) continue;

        // Создаем collapsible-line (стрелку)
        const lineContainer = document.createElement("div");
        lineContainer.className = "collapsible-line-container";
        lineContainer.setAttribute("onclick", "toggleCollapsible(this)");
        lineContainer.innerHTML = `
            <div class="collapsible-line"></div>
            <div class="collapsible-circle">
                <svg class="arrow-down" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                     stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M19 9l-7 7-7-7"/>
                </svg>
            </div>
            <div class="collapsible-line"></div>
        `;

        const collapsibleContent = document.createElement("div");
        collapsibleContent.className = "collapsible-content";

        const gridClass = gridClasses[key] || "video-grid-default";
        const grid = document.createElement("div");
        grid.className = gridClass;

        videos.forEach(src => {
            const videoItem = document.createElement("div");
            videoItem.className = "video-item";

            const video = document.createElement("video");
            video.controls = true;
            video.src = src;

            videoItem.appendChild(video);
            grid.appendChild(videoItem);
        });

        collapsibleContent.appendChild(grid);

        container.appendChild(lineContainer);
        container.appendChild(collapsibleContent);
    }
});
