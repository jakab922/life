def about_us(request, subpage, lang_code):
	if subpage not in ['recruitment', 'our_staff']:
		subpage = 'base'
		
	template_dict = generate_base_dict(lang_code, '/about_us/' + subpage + '/')
	
	template_dict['subpage'] = subpage
	
	template_dict['content_name'] = 'elements/about_us_content/' + subpage + '.html'

	if subpage in ['base', 'recruitment']:
		template_dict['real_content_id'] = 'about'
	else:
		template_dict['real_content_id'] = 'staff'
		
	if subpage == 'base':
		template_dict['container_class'] = 'page about'
	elif subpage == 'recruitment':
		template_dict['container_class'] = 'page about recruitment'
	else:
		template_dict['container_class'] = 'page staff'
	
	if subpage != 'our_staff':
		template_dict['slider_images'] = ['images/about_image.jpg', 'images/about_image_2.jpg', 'images/about_image.jpg', 'images/about_image_2.jpg']
		
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	if subpage == 'our_staff':
		template_dict['offices'] = [OfficeDummy(range(1,3)) for i in range(2)]
	
	return render_to_response('pages/about_us.html', template_dict, context_instance = RequestContext(request))