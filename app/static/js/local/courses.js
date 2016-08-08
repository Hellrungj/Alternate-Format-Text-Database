/* global Dropzone */
/* global bootbox  */
Dropzone.options.drop = {
  paramName: "file", // The name that will be used to transfer the file
  maxFilesize: 5, // MB
  acceptedFiles: ".doc,.docx,.pdf",
  accept: function(file, done) {
     done(); }
};

function delete_syllabus(form_id) {
    bootbox.confirm("Are you sure?", function(result) {
        if(result) {
           $(form_id).submit();
        }
    });
};