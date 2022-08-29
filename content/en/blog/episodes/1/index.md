---
date: 2022-08-06
title: "Announcing the podcast"
linkTitle: "Announcing the podcast"
description: "Making a new podcast"
author: Paul Cutler ([@prcutler](https://twitter.com/prcutler))
---


**This is a typical blog post that includes images.**

The front matter specifies the date of the blog post, its title, a short description that will be displayed on the blog landing page, and its author.

## Including images


The front matter of this post specifies properties to be assigned to all image resources:

```
resources:
- src: "**.{png,jpg}"
  title: "Image #:counter"
  params:
    byline: "Photo: Riona MacNamara / CC-BY-CA"
```

To include the image in a page, specify its details like this:



The image will be rendered at the size and byline specified in the front matter.


