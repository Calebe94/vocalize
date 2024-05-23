############
# vocalize #
############

.POSIX:

prefix = /usr/local
name = vocalize

install:
	@echo "Installing ${name}..."
	install -Dm555 ./${name} $(DESTDIR)/$(prefix)/bin/
	@echo "done!"

clean:
	@echo "There's nothing to clean!"

distclean: clean

uninstall:
	@echo "Uninstalling ${name}..."
	rm -f $(DESTDIR)/$(prefix)/bin/${name}
	@echo "done!"

# end
