---
title: Home
permalink: /
custom-css: 'home'
exclude-title-in-meta: true
---

<div id="splash">
    <figure>
        <video playsinline autoplay muted loop> 
            <source src="{{site.url_trailer_mp4}}" type="video/mp4">
            <source src="{{site.url_trailer_webm}}" type="video/webm">
        </video>
    </figure>
    <div id="download" class="ignore-auto-responsiveness">
        <img src="{{ site.url_logo_square }}" id="download-banner" alt="Grimhook Logo">
        <!-- <a class="button download windows font-2xl w-fit mx-auto mt-4" download> Demo Coming Soon </a> -->
        <!-- <a class="button download windows font-2xl w-fit mx-auto mt-4 hide-on-not-windows" href="{{site.demo_download_windows}}" download> <i class="fa-brands fa-windows my-auto mr-2"></i> Download The Demo </a> -->
        <a class="button download steam font-2xl w-fit mx-auto mt-4" href="/steam" target="_blank" > <i class="fa-brands fa-steam my-auto mr-2"></i><b>Play for Free!</b></a>
    </div>
</div>

<h1 class="title">About the Game</h1>

<div id="about">
    <div class="flex flex-column md:flex-row mb-10 mt-10" style="column-gap:3.7rem">
        <img src="{{ site.url_images }}/gameplay/gem.png" alt="Grimhook Logo">
        <div class="about-text">
            <h1 class="accent"> Embark on a Harrowing Journey </h1>
            <p> Grimhook thrusts you into the heart of a flooded wasteland where robotic minions reign supreme and an ancient deity lies dormant beneath the city's surface. As Dart, you'll harness powerful abilities to navigate through cavernous depths, engage in combat against foes, and discover a beautifully grim world and a somber narrative. 
            </p>
        </div>
    </div>
    <div class="flex flex-column-reverse md:flex-row" style="column-gap:3rem">
        <div class="about-text">
            <h1 class="accent"> Intense Platforming and Aerial Combat </h1>
            <p> Use your lovecraftian abilities to navigate the caverns below Miletos. Time and combine your powers to traverse the terrain and outmaneuver your enemies. Grapple, bounce, dash, and slash your way through relentless automata in multiple combat arenas, utilizing your powers to dodge bullets and decimate robotic foes.</p>
        </div>
        <img src="{{ site.url_images }}/gameplay/mines.png" alt="Grimhook Logo" class="my-auto">
    </div>
</div>

<div>
    <!-- <div id="team" class="anchor"></div> -->
    <h1 class="title"> About the Team </h1>
    {% include team.html id="team-gallery" %}
</div>

<div>
    <!-- <div id="community" class="anchor"></div> -->
    <h1 class="title"> Join the Community! </h1>
    <div class="flex flex-column md:flex-row my-12 justify-content-center">
        {% include socials.html id="community-socials" class="md:w-2/5 md:mr-6" link-class="button" icon-class="mr-1" %}
        <p class="md:w-2/5 pt-4 md:pt-0">
            Follow our socials and join our <a href="/discord" target="_blank"> Discord</a> to talk directly to devs and other fans. You'll also be the first notified about pre-release access to the game and receive sneak peeks!
        </p>
    </div>
</div>
