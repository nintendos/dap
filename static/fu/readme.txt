http://valums-file-uploader.github.io/file-uploader/



Tests
----------------------------------------------------------------------------------------------------------------------------------------															
																	Chrome-Mac	FF-Mac	Safari-Mac	Chrome-Win FF-Win	Safari-Win  IE9
- Drag file from outside of the browser should enable drop zones			
  by HTML															ok			ok		ok				ok		ok		ok			!!!
  by BODY															ok			ok		ok				ok		ok		ok			!!!
  by DIV															ok			ok		ok				ok		ok		ok			!!!
- Leave out the browser (with drag file) should disable drop zones
  by HTML															ok			ok		!!!				ok		!!!		ok			!!!
  by BODY															ok			ok		!!!				ok		!!!		ok			!!!
  by dropzone														ok			ok		!!!				ok		!!!		ok			!!!
- Drop on HTML should disable drop zones
		  BODY 														ok			ok		ok				ok		ok		ok			!!!
		  DIV														ok			ok		ok				ok		ok		ok			!!!
	      dropzone													ok			ok		ok				ok		ok		ok			!!!
	
- Cursor should change above drop zones								ok			ok		ok				ok		ok		ok			!!!
- Cursor shouldn't change anywhere else on page						ok			ok		ok				ok		!!!		ok			!!!