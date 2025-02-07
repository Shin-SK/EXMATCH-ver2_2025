$(document).ready(function() {
    // Drawer.jsの初期化
    $('.drawer').drawer();
  
    // ドロワーメニューのリンククリック時にドロワーを閉じる
    $('.drawer-menu a').on('click', function() {
      $('.drawer').drawer('close');
    });
});


$(document).ready(function() {
    // midashiの位置を取得
    var blockPosition = $('.index #midashi').offset().top; // #midashi の位置を取得
    var isVisible = false; // 現在の表示状態を保持するフラグ

    $(window).on('scroll', function() {
        var scrollTop = $(this).scrollTop(); // 現在のスクロール位置を取得
        if (scrollTop > blockPosition && !isVisible) {
            $('#navigation').addClass('visible'); // visibleクラスを付与
            isVisible = true;
        } else if (scrollTop <= blockPosition && isVisible) {
            $('#navigation').removeClass('visible'); // visibleクラスを削除
            setTimeout(() => $('#navigation').css('visibility', 'hidden'), 500); // visibilityをhiddenに
            isVisible = false;
        }
    });
});

  
$(document).ready(function () {
    $("[data-toggle='click']").on("click", function () {
        const wrap = $(this).closest(".box, .click__wrap"); // 親のwrapを取得
        const target = wrap.find("#contents"); // ターゲットの#contentsを取得

        // 表示・非表示を切り替え
        if (target.is(":hidden")) {
            target.slideDown(); // ふわっと表示
            $(this).addClass("active"); // 回転クラスを追加
        } else {
            target.slideUp(); // ふわっと非表示
            $(this).removeClass("active"); // 回転クラスを削除
        }
    });
});


$(document).ready(function() {
    // 初期表示設定
    $("#male").hide();
    $("#female").show();

    // ボタンクリック時のイベント
    $(".btn__area button").on("click", function() {
        const targetId = $(this).data("toggle"); // data-toggle の値を取得
        $(".oaite__loop").hide(); // すべて非表示
        $("#" + targetId).fadeIn(); // 対象をフェードイン
    });
});


// 1つ目のSwiper
const bannerSwiper = new Swiper('.banner', {
  slidesPerView: 1,
  spaceBetween: 20,
  centeredSlides: true,
  loop: true,
  pagination: {
      el: '.swiper-pagination',
      clickable: true,
  },
  autoplay: {
      delay: 0,
      disableOnInteraction: false,
  },
  speed: 3000,
  breakpoints: {
    768: {
        slidesPerView: 3, // 768px以下では1枚表示
        centeredSlides: false, // 中央配置を無効化
    },
},
});

// 2つ目のSwiper
const oaiteLoopSwiper = new Swiper('.oaite__loop', {
  slidesPerView: 'auto',
  spaceBetween: 20,
  loop: true,
  loopAdditionalSlides: 3, // 必要に応じて追加スライドを増やす
  autoplay: {
      delay: 0,
      disableOnInteraction: false,
  },
  speed: 3000,
  freeMode: true,
  freeModeMomentum: false,
});


const newfaceSwiper = new Swiper('.newface', {
    slidesPerView: "auto", // スライドの幅を自動調整
    spaceBetween: 16, // スライド間の余白
    loop: true, // ループ有効化
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 0,
        disableOnInteraction: false,
    },
    speed: 3000, // 自動スクロールの速度
    breakpoints: {
        768: {
            spaceBetween: 10, // 768px以下のとき、スライド間の余白を縮小
        },
    },
});

const currentPage = window.location.pathname.split("/").pop().replace(".html", ""); 
document.querySelectorAll('.nav__wrap .menu ul li a').forEach(link => {
    if (link.classList.contains(currentPage)) { 
        link.classList.add('current');
    }
});


//ファイル選択のプレビュー表示
function setupPreview(inputId, previewId, clearButtonId) {
    const input = document.getElementById(inputId);
    const preview = document.getElementById(previewId);
    const clearButton = document.getElementById(clearButtonId);

    input.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                preview.innerHTML = `<img src="${e.target.result}" alt="プレビュー画像" style="max-width: 100%; height: auto;">`;
            };
            reader.readAsDataURL(file);
        }
    });

    clearButton.addEventListener('click', function() {
        input.value = '';
        preview.innerHTML = '';
    });
}

setupPreview('formGroupLCIQDiagnosis', 'previewLCIQ', 'clearButtonLCIQ');
setupPreview('formGroupFacePhoto', 'previewFace', 'clearButtonFace');
setupPreview('formGroupPhoto1', 'previewPhoto1', 'clearButtonPhoto1');
setupPreview('formGroupPhoto2', 'previewPhoto2', 'clearButtonPhoto2');
setupPreview('formGroupPhoto3', 'previewPhoto3', 'clearButtonPhoto3');


jQuery(function($){
    $(document).ajaxSend(function() {
      $("#overlay").fadeIn(300);
    });
  
    $('#button_submit').click(function(){
      $.ajax({
        type: 'GET',
        success: function(data){
          console.log(data);
        }
      }).done(function() {
        setTimeout(function(){
          $("#overlay").fadeOut(1300);
        },500);
      });
    });
  });

  function CloseWindow() {
    window.close();
  }


  $(document).ready(function() {
    $("#open").on("click", function(e) {
        e.preventDefault();
        $("#overlay, #modal").addClass("active");

        $("#close, #overlay").on("click", function() {
            $("#overlay, #modal").removeClass("active");
            return false;
        });
    });
});


var moji = "messageID"
var tmp = document.getElementsByClassName("message") ; // クラス：messageを含む要素をtmpリストに格納

for(var i=0;i<=tmp.length-1;i++){
    //要素にid追加（messageID0～）
    tmp[i].setAttribute("id",moji+i);
    }



    function getId(ele){
        var id_value = ele.id; // eleのプロパティとしてidを取得
    //    console.log('メッセージ' + id_value); //「messageID0～」
    
      let newWindow; // 変数newWindowを宣言
      var url_ad = document.getElementById( id_value ).title;// urlアドレス取得
    
      let openBtn = document.getElementById( id_value ); // 開くボタンのidを取得
    
      openBtn.addEventListener('click', () => { // 開くボタンをクリックしたときのイベント
        newWindow = open(url_ad); // ページを開く
      });
    
        }
    