---
id: 8y9c7
title: CSS structure and rules
file_version: 1.1.2
app_version: 1.3.0
---

## Rules

1.  Use SCSS for editing styles. Never edit the compiled css files directly.
    
2.  SCSS files are organised in separate files, each encapsulating a block and its related elements and modifiers (see BEM), and imported into the main styles.scss file, which in turn is compiled into the main styles.css stylesheet.
    
3.  Use baseline CSS classes as often as possible.
    
4.  Follow the BEM style-guide rules of naming and utilisation.
    
5.  Use relative units (em), **not** absolute (px).
    

## BEM

<br/>

### Blocks

A block is an entity that is meaningful on its own.

### Elements

<br/>

### Modifiers

<br/>

## Sitemap

static<br/>
|-- styles.scss // main document, imports all subdocuments and compiles to styles.css<br/>
|-- baseline // folder for baseline stylesheets<br/>
|-- buttons.scss<br/>
|-- cards.scss<br/>
|-- navs.scss<br/>
'-- custom // folder for page-specific stylesheets<br/>
|-- teacher-new-assessment.scss

<br/>

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://app.swimm.io/repos/Z2l0aHViJTNBJTNBdnVyZGVybWVnJTNBJTNBVGhvbWFzU3RvcmhhdWc=/docs/8y9c7).