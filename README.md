# Tutorials

Various STEM related tutorials. View them [here](https://quirkycort.github.io/tutorials/)

## Editing

### Warning

* Do not edit anything in the "docs" folder. These are auto-generated by the "generate.py" script.

### Pre-requisites

* Python3
* Sass

### Folder structure

```
courses
  \_ course (dir)
    \_ section (dir)
      \_ page (markdown, .md)
```

* When generating html, all files and directories are first sorted according to their prefix number, followed by their filename.
* Files and directories starting with a "d" will be ignored.
* "template.html" may be placed in the course or section directory, where it will override the default "template.html" in the courses directory.
* "images", "css", and "js" folders may be placed in the course directory. Their content will be copied to the docs directory.
* "scss" folder may be placed in the course directory. Its content will be compiled and output placed in the corresponding css directory under "docs".