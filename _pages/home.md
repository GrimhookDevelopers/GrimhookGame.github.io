---
title: Home
permalink: /
custom-css: 'home'
exclude-title-in-meta: true
---

<div id="splash">
    <figure>
        <video playsinline autoplay muted loop> 
            <source src="/assets/videos/gameplay-short.mp4">
        </video>
    </figure>
    <div id="download" class="ignore-auto-responsiveness">
        <img src="{{ site.url_logo_1024 }}" id="download-banner" alt="Grimhook Logo">
        <a class="button download windows font-2xl w-fit mx-auto mt-4" href="{{site.demo_download_windows}}" download> <i class="fa-brands fa-windows my-auto mr-2"></i> Download The Demo </a>
    </div>
</div>

<div>
    <div id="community" class="anchor"></div>
    <h1> Join the Community! </h1>
    <div class="flex flex-column md:flex-row my-12 justify-content-center">
        {% include socials.html id="community-socials" class="md:w-2/5 md:mr-6" link-class="button" %}
        <p class="md:w-2/5 pt-4 md:pt-0">
            Follow our socials and join our <a href="/discord"> Discord</a> to talk directly to devs and other fans. You'll also be the first notified about pre-release access to the game and recieve sneak peeks!
        </p>
    </div>
</div>

<div>
    <div id="team" class="anchor"></div>
    <h1> About the Team </h1>
    {% include team.html id="team-gallery" %}
</div>
