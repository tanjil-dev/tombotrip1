(function ($) {
    "use strict";
    $(document).ready(function () {

        /* Slicknav */
        $('#nav').slicknav();

        //holy day
        $('.holy-day-carousl').owlCarousel({
            loop: true,
            autoplay: true,
            autoplayHoverPause: true,
            margin: 20,
            mouseDrag: true,
            animateIn: 'fadeIn',
            animateOut: 'fadeOut',
            nav: true,
            navText: ["<i class='fa fa-angle-double-left'></i>", "<i class='fa fa-angle-double-right'></i>"],
            responsive: {
                0: {
                    items: 1
                },
                800: {
                    items: 2
                },
                1000: {
                    items: 3
                }
            }
        });

        //holy day
        $('.video-popup').owlCarousel({
            autoplay: true,
            autoplayHoverPause: true,
            margin: 30,
            mouseDrag: true,
            nav: true,
            navText: ["<i class='fa fa-angle-double-left'></i>", "<i class='fa fa-angle-double-right'></i>"],
            responsive: {
                0: {
                    items: 1
                },
                800: {
                    items: 2
                },
                1000: {
                    items: 2
                }
            }
        });
        //price
        $("#id_end_date").datepicker({
    onSelect: function(dateText, inst) {
        var a = $("#id_start_date").datepicker('getDate').getTime(),
        b = $("#id_end_date").datepicker('getDate').getTime(),
        c = 24*60*60*1000,
        diffDays = Math.round(Math.abs((a - b)/(c)));
        var price=$("#totaldays").attr("data-id")
    var cost= ((lastday - firstday) / 86400000)*price;
    $("#totaldays").val(cost);
    }
});
//              $("#id_start_date, #id_end_date").datepicker({
//        onSelect: function (){
//
//    // Date will give time difference in miliseconds, that is why we divide with 1000*60*60*24
//    alert('got');
//    var firstday = new Date($("i#d_start_date").val().split("/").reverse().join(","));
//    var lastday = new Date($("#id_start_date").val().split("/").reverse().join(","));
//
//    var price=$("#totaldays").attr("data-id")
//    var cost= ((lastday - firstday) / 86400000)*price;
//    $("#totaldays").val(cost);
//  }
//});
        //testimonial
        $('.testimonial-2').owlCarousel({
            loop: true,
            autoplay: true,
            autoplayHoverPause: true,
            margin: 20,
            mouseDrag: true,
            animateIn: 'fadeIn',
            animateOut: 'fadeOut',
            nav: true,
            navText: ["<i class='fa fa-angle-double-left'></i>", "<i class='fa fa-angle-double-right'></i>"],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 2
                }
            }
        });



        //photo-list of product
        $('.photo-list').owlCarousel({
            loop: true,
            autoplay: true,
            autoplayHoverPause: true,
            margin: 20,
            mouseDrag: true,
            nav: true,
            navText: ["<i class='fa fa-angle-double-left'></i>", "<i class='fa fa-angle-double-right'></i>"],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 1
                }
            }
        });


        //photo-list of product
        $('.about-team-tt').owlCarousel({
            loop: true,
            autoplay: true,
            autoplayHoverPause: true,
            margin: 10,
            mouseDrag: true,
            nav: true,
            navText: ["<i class='fa fa-angle-double-left'></i>", "<i class='fa fa-angle-double-right'></i>"],
            responsive: {
                0: {
                    items: 1
                },
                400: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 2
                }
            }
        });


        //date picker
        $("#datepicker1").datepicker();
        $("#datepicker2").datepicker();






        /* Scroll-Top */
        $(".scroll").hide();

        $(window).scroll(function () {
            if ($(this).scrollTop() > 300) {
                $(".scroll").fadeIn();
            } else {
                $(".scroll").fadeOut();
            }
        });

        $(".scroll").click(function () {
            $("html, body").animate({
                scrollTop: 0,
            }, 550)
        });

        //filter-price
        $("#filter").slider({
            range: true,
            min: 10,
            max: 2000,
            values: [99, 399],
            slide: function (event, ui) {
                $("#show").html(ui.values[0] + '$' + '-' + ui.values[1] + '$');
            }
        });
        $("#show").html($("#filter").slider('values', 0) + '$' + '-' + $("#filter").slider('values', 1) + '$');

        // Magnific Popup Video
        $(".mgVideo").magnificPopup({
            type: 'iframe',
            iframe: {
                markup: '<div class="mfp-iframe-scaler">' +
                    '<div class="mfp-close"></div>' +
                    '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
                    '</div>',
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: 'v=',
                        src: 'https://www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: '/',
                        src: 'https://player.vimeo.com/video/%id%?autoplay=1'
                    },
                    gmaps: {
                        index: '//maps.google.',
                        src: '%id%&output=embed'
                    }
                },
                srcAction: 'iframe_src',
            }
        });

        $(".table-row").click(function () {
            window.document.location = $(this).data("href");
        });

        //address input
        (function () {
            var placesAutocomplete = places({
                appId: 'plEHFE8OXN3L',
                apiKey: 'a6eb12d44e181f3c3c3d02bd7cf7b2fd',
                container: document.querySelector('#address')
            });

            var $address = document.querySelector('#address-value')
            placesAutocomplete.on('change', function (e) {
                $address.textContent = e.suggestion.value
            });

            placesAutocomplete.on('clear', function () {
                $address.textContent = 'none';
            });

        })();
        //        $('#myModal').on('shown.bs.modal', function () {
        //            $('#video1')[0].play();
        //        })
        //        $('#myModal').on('hidden.bs.modal', function () {
        //            $('#video1')[0].pause();
        //        })

        //        $(window).scroll(function () {
        //            if ($(this).scrollTop() > 50) {
        //                $('#back-to-top').fadeIn();
        //            } else {
        //                $('#back-to-top').fadeOut();
        //            }
        //        });
        //        // scroll body to 0px on click
        //        $('#back-to-top').click(function () {
        //            $('#back-to-top').tooltip('hide');
        //            $('body,html').animate({
        //                scrollTop: 0
        //            }, 800);
        //            return false;
        //        });
        //
        //        $('#back-to-top').tooltip('show');





    });

})(jQuery);

        //faq collapse
        $('.collapse').collapse();





        /* Scroll-Top */
        $(".scroll").hide();

        $(window).scroll(function () {
            if ($(this).scrollTop() > 300) {
                $(".scroll").fadeIn();
            } else {
                $(".scroll").fadeOut();
            }
        });

        $(".scroll").click(function () {
            $("html, body").animate({
                scrollTop: 0,
            }, 550)
        });

        //filter-price
        $("#filter").slider({
            range: true,
            min: 10,
            max: 2000,
            values: [99, 399],
            slide: function (event, ui) {
                $("#show").html(ui.values[0] + '$' + '-' + ui.values[1] + '$');
            }
        });
        $("#show").html($("#filter").slider('values', 0) + '$' + '-' + $("#filter").slider('values', 1) + '$');

        // Magnific Popup Video
        $(".mgVideo").magnificPopup({
            type: 'iframe',
            iframe: {
                markup: '<div class="mfp-iframe-scaler">' +
                    '<div class="mfp-close"></div>' +
                    '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
                    '</div>',
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: 'v=',
                        src: 'https://www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: '/',
                        src: 'https://player.vimeo.com/video/%id%?autoplay=1'
                    },
                    gmaps: {
                        index: '//maps.google.',
                        src: '%id%&output=embed'
                    }
                },
                srcAction: 'iframe_src',
            }
        });

        $(".table-row").click(function () {
            window.document.location = $(this).data("href");
        });

        //address input
        (function () {
            var placesAutocomplete = places({
                appId: 'plEHFE8OXN3L',
                apiKey: 'a6eb12d44e181f3c3c3d02bd7cf7b2fd',
                container: document.querySelector('#address')
            });

            var $address = document.querySelector('#address-value')
            placesAutocomplete.on('change', function (e) {
                $address.textContent = e.suggestion.value
            });

            placesAutocomplete.on('clear', function () {
                $address.textContent = 'none';
            });

        })();
        //        $('#myModal').on('shown.bs.modal', function () {
        //            $('#video1')[0].play();
        //        })
        //        $('#myModal').on('hidden.bs.modal', function () {
        //            $('#video1')[0].pause();
        //        })

        //        $(window).scroll(function () {
        //            if ($(this).scrollTop() > 50) {
        //                $('#back-to-top').fadeIn();
        //            } else {
        //                $('#back-to-top').fadeOut();
        //            }
        //        });
        //        // scroll body to 0px on click
        //        $('#back-to-top').click(function () {
        //            $('#back-to-top').tooltip('hide');
        //            $('body,html').animate({
        //                scrollTop: 0
        //            }, 800);
        //            return false;
        //        });
        //
        //        $('#back-to-top').tooltip('show');





    });

})(jQuery);
