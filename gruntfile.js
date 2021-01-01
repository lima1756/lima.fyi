module.exports = function (grunt) {
    grunt.initConfig({
        // Variables
        paths: {
            src: 'src',
            src_resources: 'src/resources',
            build: 'build',
            input: {
                js: 'src/**/*.js',
                css: 'src/resources/css/*.css'
            },
            output: {
                js: 'build/resources/js/main.js',
                jsmin: 'build/resources/js/main.min.js',
                css: 'build/resources/css/style.css',
                cssmin: 'build/resources/css/style.min.css'
            }

        },
        // Tasks
        clean: ['<%= paths.build %>'],
        concat: {
            js: {
                src: [
                    '<%= paths.src_resources %>/js/jquery.min.js',
                    '<%= paths.src_resources %>/js/modernizr.custom.js',
                    '<%= paths.src_resources %>/js/animating.js',                    
                    '<%= paths.input.js %>',
                    '!<%= paths.src_resources %>/js/main.js',
                    '!<%= paths.src_resources %>/js/validator.js',
                    '!<%= paths.src_resources %>/js/jquery.magnific-popup.min.js',
                    '<%= paths.src_resources %>/js/jquery.magnific-popup.min.js',
                    '<%= paths.src_resources %>/js/validator.js',
                    '<%= paths.src_resources %>/js/main.js',
                ],
                dest: '<%= paths.output.js %>'
            },
            css: {
                src: ['<%= paths.src_resources %>/css/main.css', '<%= paths.input.css %>'],
                dest: '<%= paths.output.css %>'
            }
        },
        copy: {
            main: {
                files: [
                    { expand: true, cwd: '<%= paths.src %>', src: ['*.html'], dest: 'build/', filter: 'isFile' },
                    { expand: true, cwd: '<%= paths.src %>', src: ['resources/static/**'], dest: 'build' },
                ],
            },
        },
        cssmin: {
            options: {
                inline: false
            },
            css: {
                src: '<%= concat.css.dest %>',
                dest: '<%= paths.output.cssmin %>'
            }
        },
        htmlmin: {
            dist: {
                options: {
                    removeComments: true,
                    collapseWhitespace: true
                },
                files: {
                    'build/index.html': 'build/index.html',
                    'build/error.html': 'build/error.html',
                }
            },
        },
        shell: {
            publish: {
                command: 'aws s3 sync . s3://lima.fyi',
                options: {
                    stderr: false,
                    execOptions: {
                        cwd: 'build'
                    }
                }
            }
        },
        uglify: {
            js: {
                files: {
                    '<%= paths.output.jsmin %>': ['<%= concat.js.dest %>']
                }
            }
        },
        useminPrepare: {
            html: ['<%= paths.src %>/index.html', '<%= paths.src %>/error.html'],
            options: {
                dest: '<%= paths.build %>'
            }
        },
        usemin: {
            html: ['<%= paths.build %>/index.html', '<%= paths.build %>/error.html'],
        },
    });

    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-htmlmin');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-shell');
    grunt.loadNpmTasks('grunt-usemin');

    grunt.registerTask('default', ['clean', 'copy', 'useminPrepare', 'concat', 'uglify', 'cssmin', 'usemin', 'htmlmin', 'shell']);
};