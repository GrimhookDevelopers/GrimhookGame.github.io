---
title: Home
permalink: /
custom-css: 'home'
exclude-title-in-meta: true
---

<div id="splash">
    <figure>
        <video playsinline autoplay muted loop> 
            <source src="/assets/videos/gameplay-short.mp4" type="video/mp4">
            <source src="/assets/videos/gameplay-short.webm" type="video/webm">
        </video>
    </figure>
    <div id="download" class="ignore-auto-responsiveness">
        <img src="{{ site.url_logo_1024 }}" id="download-banner" alt="Grimhook Logo">
        <a class="button download windows font-2xl w-fit mx-auto mt-4" download> Demo Coming Soon </a>
        <!-- <a class="button download windows font-2xl w-fit mx-auto mt-4 hide-on-not-windows" href="{{site.demo_download_windows}}" download> <i class="fa-brands fa-windows my-auto mr-2"></i> Download The Demo </a> -->
        <!-- <a class="button download steam font-2xl w-fit mx-auto mt-4 hide-on-windows" href="{{site.download_steam}}" download> <i class="fa-brands fa-steam my-auto mr-2"></i> Steam </a> -->
    </div>
</div>

<div>
    <!-- <div id="about" class="anchor"></div>
    <h1> About the Project </h1>
    <p>
        Look, just because I don't be givin' no man a foot massage don't make it right for Marsellus to throw Antwone into a glass motherfuckin' house, fuckin' up the way the nigger talks. Motherfucker do that shit to me, he better paralyze my ass, 'cause I'll kill the motherfucker, know what I'm sayin'?
    </p>
    <p>
        My money's in that office, right? If she start giving me some bullshit about it ain't there, and we got to go someplace else and get it, I'm gonna shoot you in the head then and there. Then I'm gonna shoot that bitch in the kneecaps, find out where my goddamn money is. She gonna tell me too. Hey, look at me when I'm talking to you, motherfucker. You listen: we go in there, and that nigga Winston or anybody else is in there, you the first motherfucker to get shot. You understand?
    </p>
    <p>
        The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who would attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee.
    </p>
</div> -->

<div>
    <div id="team" class="anchor"></div>
    <h1> About the Team </h1>
    {% include team.html id="team-gallery" %}
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
