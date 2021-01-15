// $("form[name=signup_form]").submit(function (e) {
//   var $form = $(this);
//   var $error = $form.find(".error");
//   var data = $form.serialize();
//   console.log(data);
//   $.ajax({
//     url: "/user/signup",
//     type: "POST",
//     data: data,
//     dataType: "json",
//     success: function (resp) {
//       window.location.href = "/dashboard/";
//     },
//     error: function (resp) {
//       $error.text(resp.responseJSON.error).removeClass("error--hidden");
//     },
//   });

//   e.preventDefault();
// });

1;
2;
3;
4;
$("#signup").on("submit", function (event) {
  event.preventDefault();
  console.log($(this).serialize());
});
