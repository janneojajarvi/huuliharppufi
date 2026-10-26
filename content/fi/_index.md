---
title: "Tervetuloa Huuliharppu.fi-sivustolle"
draft: false
date: 2023-01-01T00:00:00+02:00
description: "Huuliharppu.fi on suomalainen huuliharppusivusto, jolta löydät tietoa huuliharpunsoitosta, soittimien huollosta ja säädöstä sekä o"
---

Huuliharppu.fi on suomalainen huuliharppusivusto, jolta löydät tietoa huuliharpunsoitosta, soittimien huollosta ja säädöstä sekä oppimateriaalia ja tietoa soitonopetuksesta.

<b>Video of the month</b>
<div id="monthly-video-container" style="margin: 20px 0;">
<!-- Kuukauden video latautuu tähän -->
</div>

<script>
// Lista YouTube-videoiden ID:istä (voit lisätä tähän niin paljon videoita kuin haluat)
const monthlyVideos = [
"DKKNMHmeR6o",
"5t-qWjMvVv8",
"wOHvr8DJtXA",
"DGZRuYPvUGc",
"jjuXNGAau8o",
"8QqJAxE2E5o",
"n45fvWFhXJU",
"2rx8kVBjAL4",
"jHfJLhBV1e8",
"i1F_eQkOfvU",
"uIss2Qmmc5k",
"DGZRuYPvUGc",
"b3lTzDqfihk",
"uOZe3HTqvgM",
"BQuLIfq0Tac",
"LN2vrmduTYQ",
"jb1JlBDqsSU",
"3K2xao0RJeo",
"gKrz3WWQtto",
"WciSPzZtUqM",
"vRG8yf10WhM",
"YxYCGdTowl0",
"XlTSU7pLrLk",
"yAiSmGJQGlA",
"qvdpFP28VJc",
"4G1p18y0EF0",
"fMlIq6HjxZg",
"ERBPdJ57D-s",
"k05Wkbz9MJY"
// Lisää tähän halutessasi lisää video-ID:itä pilkulla erotettuna, esim:
// "TOINEN_VIDEO_ID",
// "KOLMAS_VIDEO_ID"
 ];

// Lasketaan kuukausi-indeksi (vuosi * 12 + kuukausi), jotta video vaihtuu aina kerran kuukaudessa
const now = new Date();
const totalMonths = now.getFullYear() * 12 + now.getMonth();
const monthIndex = totalMonths % monthlyVideos.length;
const selectedVideoId = monthlyVideos[monthIndex];

// Upotetaan iframe sivulle dynaamisesti
const container = document.getElementById('monthly-video-container');
container.innerHTML = `<iframe width="100%" height="450" src="https://www.youtube-nocookie.com/embed/${selectedVideoId}" title="Kuukauden video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
</script>
