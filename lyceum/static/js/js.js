function team_scroll() {
    $(document).ready(function(){
        $('.item_nav_link').click( function(){
        var scroll_el = $(this).attr('href'); // возьмем содержимое атрибута href, должен быть селектором, т.е. например начинаться с # или .
            if ($(scroll_el).length != 0) { // проверим существование элемента чтобы избежать ошибки
            $('html, body').animate({ scrollTop: $(scroll_el).offset().top - 160 }, 1500); // анимируем скроолинг к элементу scroll_el
            }
            return false; // выключаем стандартное действие
        });
    });
}
/**
 * Created by oleg on 26.12.2016.
 */
function calendar(){
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    });
    $('.ro-select').filter(function(){
  var $this = $(this),
      $sel = $('<ul>',{'class': 'ro-select-list'}),
      $wr = $('<div>', {'class': 'ro-select-wrapper'}),
      $inp = $('<input>', {
        type:'hidden',
        name: $this.attr('name'),
        'class': 'ro-select-input'
      }),
      $text = $('<div>', {
        'class':'ro-select-text ro-select-text-empty',
        'name': $inp[0].name,
        text: $this.attr('placeholder')
      });
      $opts = $this.children('option');
  $text.click(function(){
    $sel.show();
  });

  $opts.filter(function(){
    var $opt = $(this);
    $sel.append($('<li>',{text:$opt.text(), 'class': 'ro-select-item','name': $inp[0].name})).data('value',$opt.attr('value'));
  });
  $sel.on('click','li',function(){
    $text.text($(this).text()).removeClass('ro-select-text-empty');
    $(this).parent().hide().children('li').removeClass('ro-select-item-active');
    $(this).addClass('ro-select-item-active');
    $inp.val($this.data('value'));
  });
  $wr.append($text);
  $wr.append($('<i>', {'class':'fa fa-caret-down ro-select-caret'}));
  $this.after($wr.append($inp,$sel));
  $this.remove();
});
    get_year();
    get_month(0);
    next_month();
    prev_month();
    slideheader();
   // slidecalendar();
    $("#tel").mask("8 (999) 999-99-99");
    $("#tel2").mask("8 (999) 999-99-99");
    warning_offer();
    warning_com();
    team_scroll();
}
function warning_offer(){
    if($("div.warning_o[name='name']").text() != ""){
        $("input[name='o_name']").css("border-bottom","1px solid red")
    }
    if($("div.warning_o[name='email']").text() != ""){
        $("input[name='o_email']").css("border-bottom","1px solid red")
    }
    if($("div.warning_o[name='topic']").text() != ""){
        $("input[name='o_topic']").css("border-bottom","1px solid red")
    }
    if($("div.warning_o[name='phone']").text() != ""){
        $("input[name='tel']").css("border-bottom","1px solid red")
    }
    if($("div.warning_o[name='text']").text() != ""){
        $("textarea[name='o_text']").css("border-bottom","1px solid red")
    }
}
function warning_com(){
    if($("div.warning_c[name='name']").text() != ""){
        $("input[name='c_name']").css("border-bottom","1px solid red")
    }
    if($("div.warning_c[name='email']").text() != ""){
        $("input[name='c_email']").css("border-bottom","1px solid red")
    }
    if($("div.warning_c[name='topic']").text() != ""){
        $("input[name='c_topic']").css("border-bottom","1px solid red")
    }
    if($("div.warning_c[name='phone']").text() != ""){
        $("input[name='tel2']").css("border-bottom","1px solid red")
    }
    if($("div.warning_c[name='text']").text() != ""){
        $("textarea[name='c_text']").css("border-bottom","1px solid red")
    }
}
function get_year() {
    $(document).ready(function(){
        $(".ro-select-item[name='year']").bind("click", function(){
            year = $(this).text();
            month = $(".ro-select-text[name='month']").text();
            switch (month){
                case 'Январь': month = 1; break;
                case 'Февраль': month = 2; break;
                case 'Март': month = 3; break;
                case 'Апрель': month = 4; break;
                case 'Май': month = 5; break;
                case 'Июнь': month = 6; break;
                case 'Июль': month = 7; break;
                case 'Август': month = 8; break;
                case 'Сентябрь': month = 9; break;
                case 'Октябрь': month = 10; break;
                case 'Ноябрь': month = 11; break;
                case 'Декабрь': month = 12; break;
            }
            $.get("", {year: year, month: month}, function(data){
                $('div.calendar').empty();
                $('div.calendar').html(data);
            })
        });
    });
}
function slideheader(){
    $(document).scroll(function () {
        if ($(document).scrollTop() > $('header').height()){
           $('header').addClass("fixed");
            $('header').css("height","50px");
            $('header').css("line-height","100%");
            $('.header_logo').css("line-height","200%");
            $('.menu').css("margin-top","5px");
        }
        else {
            $('header').removeClass("fixed");
            $('header').css("height","70px");
            $('header').css("line-height","200%");
            $('.header_logo').css("line-height","300%");
            $('.menu').css("margin-top","20px");
        }
    })
}
function slidecalendar(){
    $(document).scroll(function () {
        if ($(document).scrollTop() > $('header').height()){
           $('.desk_of_events').addClass("fixed");
            $('.desk_of_events').css("margin-top","80px");
        }
        else {
            $('.desk_of_events').removeClass("fixed");
            $('.desk_of_events').css("margin-top","0");
        }
    })
}
function news_addition(){
    var $i = 2;

    $(document).ready(function(){
        $("i#news_addition").on("click",function(){
            if($i % 2 == 0) {
                $(this).removeClass('fa fa-angle-down');
                $(this).addClass('fa fa-angle-up');
                $i = 3;
            }
            else{
                $(this).removeClass('fa fa-angle-up');
                $(this).addClass('fa fa-angle-down');
                $i = 2;
            }
        })
    });
}
function tran_header() {
    $('header').css("background","transparent");
     $('header').css("position","fixed");
     $('.content').css("margin-top","100px");
     $(document).scroll(function () {
         if ($(document).scrollTop() > $('header').height()) {
             $('header').css("background","#293a48");
         }
         else {
             $('header').css("background","transparent");
         }
      });
}
function next_month(){
    $(document).ready(function(){
        $(".next_month").on("click", function(){
            year = $(".ro-select-text[name='year']").text();
            year = Number(year);
            month = $(".ro-select-text[name='month']").text();
            switch (month){
                case 'Январь': month = 1; break;
                case 'Февраль': month = 2; break;
                case 'Март': month = 3; break;
                case 'Апрель': month = 4; break;
                case 'Май': month = 5; break;
                case 'Июнь': month = 6; break;
                case 'Июль': month = 7; break;
                case 'Август': month = 8; break;
                case 'Сентябрь': month = 9; break;
                case 'Октябрь': month = 10; break;
                case 'Ноябрь': month = 11; break;
                case 'Декабрь': month = 12; break;
            }
            month = month + 1;
            if (month == 13){
                month = 1;
                year = year + 1;
            }
            $.get("", {year: year, month: month}, function(data){
               $('#cal').addClass('animated fadeOutLeft');
                setTimeout(function () {
                    $('div.calendar').empty();
                    $('div.calendar').html(data);
                    $('#cal').addClass('animated fadeInRight');
                }, 400);
            })
        });
    });
}
function prev_month(){
    $(document).ready(function(){
        $(".previous_month").on("click", function(){
            year = $(".ro-select-text[name='year']").text();
            year = Number(year);
            month = $(".ro-select-text[name='month']").text();
            switch (month){
                case 'Январь': month = 1; break;
                case 'Февраль': month = 2; break;
                case 'Март': month = 3; break;
                case 'Апрель': month = 4; break;
                case 'Май': month = 5; break;
                case 'Июнь': month = 6; break;
                case 'Июль': month = 7; break;
                case 'Август': month = 8; break;
                case 'Сентябрь': month = 9; break;
                case 'Октябрь': month = 10; break;
                case 'Ноябрь': month = 11; break;
                case 'Декабрь': month = 12; break;
            }
            month = month - 1;
            if (month == 0){
                month = 12;
                year = year - 1;
            }
            $.get("", {year: year, month: month}, function(data){
                $('#cal').addClass('animated fadeOutRight');
                setTimeout(function () {
                    $('div.calendar').empty();
                    $('div.calendar').html(data);
                    $('#cal').addClass('animated fadeInLeft');
                }, 400);
            });
        });
    });
}
function send_mail(){
    prob = '                                                                                                               ';
    var errors=0;
   $("button[name='send_email']").on("click", function () {
        name = $('input[name="send_name"]').val();
        if ((name.charAt(0) == "") || (name.charAt(0) == " ")){
           $('input[name="send_name"]').css("border-bottom","1px solid red");
           errors += 1;
        }
        else{
            $('input[name="send_name"]').css("border-bottom","1px solid #ccc");
        }
        email = $('input[name="send_email"]').val();
        if ((name.charAt(0) == "") || (name.charAt(0) == " ")){
           $('input[name="send_email"]').css("border-bottom","1px solid red");
           errors += 1;
        }
        else{
            $('input[name="send_email"]').css("border-bottom","1px solid #ccc");
        }
        topic = $('input[name="send_topic"]').val();
        if ((name.charAt(0) == "") || (name.charAt(0) == " ")){
           $('input[name="send_topic"]').css("border-bottom","1px solid red");
           errors += 1;
        }
        else{
            $('input[name="send_topic"]').css("border-bottom","1px solid #ccc");
        }
        text = $('textarea[name="send_mail_text"]').val();
        if ((name.charAt(0) == "") || (name.charAt(0) == " ")){
           $('textarea[name="send_mail_text"]').css("border-bottom","1px solid red");
           errors += 1;
        }
        else{
            $('textarea[name="send_mail_text"]').css("border-bottom","1px solid #ccc");
        }
        if (errors == 0){
            $.post('/send_email/',{send_email:email,send_name:name, send_text:text, send_topic:topic}, function (data) {
                $('input[name="send_name"]').val("");
                $('input[name="send_email"]').val("");
                $('textarea[name="send_mail_text"]').val("");
                $('input[name="send_topic"]').val("");
                $(".alert").show();
                $(".alert").addClass("fadeInRight");
                setTimeout(function () {
                    $(".alert").removeClass("fadeInRight");
                    setTimeout(function () {
                        $(".alert").addClass("fadeOutRight");
                        setTimeout(function () {
                            $(".alert").hide()
                        }, 800);
                    }, 10000);
                }, 800);
            });
        }
        errors = 0;
   });
}
function get_month(next){
    $(document).ready(function(){
        $(".ro-select-item[name='month']").bind("click", function(){
            year = $(".ro-select-text[name='year']").text();
            month = $(this).text();
            if (next == 1){
                month = Number(month) + 1;
                alert(month);
            }
            switch (month){
                case 'Январь': month = 1; break;
                case 'Февраль': month = 2; break;
                case 'Март': month = 3; break;
                case 'Апрель': month = 4; break;
                case 'Май': month = 5; break;
                case 'Июнь': month = 6; break;
                case 'Июль': month = 7; break;
                case 'Август': month = 8; break;
                case 'Сентябрь': month = 9; break;
                case 'Октябрь': month = 10; break;
                case 'Ноябрь': month = 11; break;
                case 'Декабрь': month = 12; break;
            }
            $.get("", {year: year, month: month}, function(data){
                $('div.calendar').empty();
                $('div.calendar').html(data);
            })
        });
    });
}