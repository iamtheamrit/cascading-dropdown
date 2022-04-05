const emptyOption = $("<option value=''>---------</option>");

function fetchOptions(id,data,childId=null){
    var url = $(id).attr("data-url");
    $.ajax({
      url: url,                 
      data: data,
      success: function (data) {
        $(id).html(data);
        if (childId){
            $(childId).html(emptyOption);
        }
      }
    });
}

if ($("#id_state").val()){
    fetchOptions("#id_district",{
        'state': $("#id_state").val()
      },"#id_village",)
}
$("#id_state").change(function () {
    fetchOptions("#id_district",{
        'state': $(this).val()
      },"#id_village",)
});

// $("#id_district").change(function () {
//     fetchOptions("#id_village",{
//         'district': $(this).val()
//       })
// });

$("#id_district").change(function () {
  var url = $("#id_village").attr("data-url") + $(this).val();
  $("#id_village").html(emptyOption);
    $.ajax({
      url: url,                 
      success: function (data) {
        for (var i = 0; i < data.length; i++) {
            var option = $("<option value='" + data[i].pk + "'>" + data[i].name + "</option>");
            $("#id_village").append(option);
        }
      }
    });
});
