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

<!-- delete this line @ian
<div id="about">
    <div class="flex flex-column md:flex-row mb-10">
        <img src="https://images.squarespace-cdn.com/content/v1/606d4bb793879d12d807d4c8/1617943241416-WVIDZ5G6CQKP6YS7122Y/website_mini_0000_mini3.jpg" alt="Grimhook Logo">
        <div>
            <h1> Captured and Taken to a Distant Land </h1>
            <p> Hornet, princess-protector of Hallownest, finds herself alone in a vast, unfamiliar world. </p>
            <p> She must battle foes, seek out allies, and solve mysteries as she ascends on a deadly pilgrimage to the kingdom’s peak. </p>
            <p> Bound by her lineage and guided by echoes of her past, Hornet will adventure through mossy grottos, coral forests and shining citadels to unravel a deadly thread that threatens this strange new land. </p>
        </div>
    </div>
    <div class="flex flex-column-reverse md:flex-row">
        <div>
            <h1> Captured and Taken to a Distant Land </h1>
            <p> Hornet, princess-protector of Hallownest, finds herself alone in a vast, unfamiliar world. </p>
            <p> She must battle foes, seek out allies, and solve mysteries as she ascends on a deadly pilgrimage to the kingdom’s peak. </p>
            <p> Bound by her lineage and guided by echoes of her past, Hornet will adventure through mossy grottos, coral forests and shining citadels to unravel a deadly thread that threatens this strange new land. </p>
        </div>
        <img src="https://images.squarespace-cdn.com/content/v1/606d4bb793879d12d807d4c8/1617943241416-WVIDZ5G6CQKP6YS7122Y/website_mini_0000_mini3.jpg" alt="Grimhook Logo" class="my-auto">
    </div>
</div>
also delete this line-->

<div>
    <div id="team" class="anchor"></div>
    <h1> About the Team </h1>
    {% include team.html id="team-gallery" %}
</div>

<div>
    <!-- <div id="community" class="anchor"></div> -->
    <h1> Join the Community! </h1>
    <div class="flex flex-column md:flex-row my-12 justify-content-center">
        {% include socials.html id="community-socials" class="md:w-2/5 md:mr-6" link-class="button" icon-class="mr-1" %}
        <p class="md:w-2/5 pt-4 md:pt-0">
            Follow our socials and join our <a href="/discord" target="_blank"> Discord</a> to talk directly to devs and other fans. You'll also be the first notified about pre-release access to the game and receive sneak peeks!
        </p>
    </div>
</div>
