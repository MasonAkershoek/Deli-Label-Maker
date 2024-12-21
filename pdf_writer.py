import pypdf
import pdfrw
import tempfile
import globs
from tkinter import messagebox

def fill_single_page_pdf(input_path, output_path, field_values):
    try:
        with open(input_path, 'rb') as pdf_file:
            pdf_reader = pypdf.PdfReader(pdf_file)
            pdf_writer = pypdf.PdfWriter()

            #pdf_writer.set_need_appearances_writer(True)


            page = pdf_reader.pages[0]

            pdf_writer.append(pdf_reader)

            pdf_writer.update_page_form_field_values(
                pdf_writer.pages[0],
                field_values,
                auto_regenerate=True,
            )

            # Get form fields
            #pdf_writer.update_page_form_field_values(pdf_writer.pages[0], field_values)

            # Write filled PDF to output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            

            pdf = pdfrw.PdfReader(output_path)
            for page in pdf.pages:
                annotations = page.get("/Annots")
                if annotations:
                    for annotation in annotations:
                        annotation.update(pdfrw.PdfDict(AP=""))
                                    
            pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
            pdfrw.PdfWriter().write(output_path, pdf)
            messagebox.showinfo("Success", "The PDF has been filled successfully.")
            return output_path
    except Exception as e:
        messagebox.showerror("Error", "An error occurred while trying to fill the PDF. Please try again.")

