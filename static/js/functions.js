
/*
Modal Functionalitiy
*/

function openCustomModal(url) {
  $('#custom-modal').load(url, function() {
    $(this).modal('show');
  });
  return false;
}

function closeCustomModal() {
  $('#custom-modal').modal('hide');
  return false;

}

/*
*/

function walkTheDOM(node, func) {
    func(node);
    node = node.firstChild;
    while (node) {
        walkTheDOM(node, func);
        node = node.nextSibling;
    }
}

function replaceCopy(node) {
  function replaceNode(currentNode) {

    var num_forms = document.getElementsByClassName("period-schedule-form-class");
    var total_forms = document.getElementById("id_form-TOTAL_FORMS");
    total_forms.value = num_forms.length + 1;

    // ID's
    if (currentNode.id == "period-schedule-form-0") {
      currentNode.id = "period-schedule-form-" + num_forms.length;
    }
    if (currentNode.id == "id_form-0-inicio") {
      currentNode.id = "id_form-" + num_forms.length + "-inicio";
    }
    if (currentNode.id == "id_form-0-fin") {
      currentNode.id = "id_form-" + num_forms.length + "-fin";
    }

    // Names's
    if (currentNode.name == "form-0-inicio") {
      currentNode.name = "form-" + num_forms.length + "-inicio";
    }
    if (currentNode.name == "form-0-fin") {
      currentNode.name = "form-" + num_forms.length + "-fin";
    }

    // Checked
    /*
    currentNode.find(':input').each(function() {
      var id = 'id_' + name;
      $(this).removeAttr('checked');
    });
    */
  }

  walkTheDOM(node, replaceNode);

  return node;
}

$(document).on('click', '.delete-form', function() {
  console.log("delete period schedule form")

  var form_id = ($(this).attr("data-target"))
  var form = document.getElementById("period-schedule-form-" + form_id);
  var formset = document.getElementById("period-schedule-formset");

  formset.removeChild(form);

  var total_forms = document.getElementById("id_form-TOTAL_FORMS");
  total_forms.value = total_forms.value - 1;

});

$(document).on('click', '.add-form', function(e) {
  console.log("clone period schedule form")

  e.preventDefault();

  var form = document.getElementById("period-schedule-form-0");
  var formset = document.getElementById("period-schedule-formset");
  var copy = form.cloneNode(true);

  formset.appendChild(replaceCopy(copy));
});
