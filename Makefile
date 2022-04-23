
PYRCTGEN_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
ifeq (,$(PACKAGES_DIR))
  PACKAGES_DIR := $(PYRCTGEN_DIR)/packages
endif

export PACKAGES_DIR

$(PACKAGES_DIR)/python :
	ivpm update

pdf : $(PACKAGES_DIR)/python
	$(PACKAGES_DIR)/python/bin/sphinx-build -M latexpdf \
		$(PYRCTGEN_DIR)/doc/source \
		build

html : $(PACKAGES_DIR)/python
	$(PACKAGES_DIR)/python/bin/sphinx-build -M html \
		$(PYRCTGEN_DIR)/doc/source \
			build

clean :
	rm -rf build 

