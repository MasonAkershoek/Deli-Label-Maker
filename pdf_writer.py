import pypdf
import pdfrw

def fill_single_page_pdf(input_path, output_path, field_values):
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
        print(output_path)
        return output_path

def tk_interface(chef_name, dish_title, price, weight, experation, blank, ingredients, desktop, blanks_folder):
    
    input_pdf_path = blanks_folder + blank
    output_pdf_path = desktop + dish_title + "_" + chef_name + ".pdf"
    

    field_values = {
        't1' : dish_title,
        't2' : dish_title,
        't3' : dish_title,
        't4' : dish_title,
        't5' : dish_title,
        't6' : dish_title,
        't7' : dish_title,
        't8' : dish_title,
        't9' : dish_title,
        't10' : dish_title,
        'i1' : ingredients,
        'i2' : ingredients,
        'i3' : ingredients,
        'i4' : ingredients,
        'i5' : ingredients,
        'i6' : ingredients,
        'i7' : ingredients,
        'i8' : ingredients,
        'i9' : ingredients,
        'i10' : ingredients, 
        'w1' : weight,
        'w2' : weight,
        'w3' : weight,
        'w4' : weight,
        'w5' : weight,
        'w6' : weight,
        'w7' : weight,
        'w8' : weight,
        'w9' : weight,
        'w10' : weight,
        'p1' : price,
        'p2' : price,
        'p3' : price,
        'p4' : price,
        'p5' : price,
        'p6' : price,
        'p7' : price,
        'p8' : price,
        'p9' : price,
        'p10' : price,
        'e1' : experation,
        'e2' : experation,
        'e3' : experation,
        'e4' : experation,
        'e5' : experation,
        'e6' : experation,
        'e7' : experation,
        'e8' : experation,
        'e9' : experation,
        'e10' : experation,
    }

    return fill_single_page_pdf(input_pdf_path, output_pdf_path, field_values)
