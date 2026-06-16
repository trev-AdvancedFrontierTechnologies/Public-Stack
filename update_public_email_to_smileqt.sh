#!/usr/bin/env bash
set -Eeuo pipefail

OLD_EMAIL="trev@smileqt.com"
NEW_EMAIL="trev@smileqt.com"
STAMP="$(date +%Y%m%d_%H%M%S)"

echo "== Updating public email to $NEW_EMAIL =="

###############################################################################
# Live company site
###############################################################################

SITE_DIR="$HOME/aft_company_site"
WEB_DIR="$SITE_DIR/site"

if [ -d "$WEB_DIR" ]; then
  echo "== Updating live company site =="
  mkdir -p "$SITE_DIR/backups"
  tar czf "$SITE_DIR/backups/site_before_email_change_${STAMP}.tgz" -C "$SITE_DIR" site

  grep -RIl "$OLD_EMAIL" "$WEB_DIR" | while read -r f; do
    echo "Updating $f"
    sed -i "s#$OLD_EMAIL#$NEW_EMAIL#g" "$f"
  done

  docker exec aft_company_site nginx -s reload >/dev/null 2>&1 || docker restart aft_company_site >/dev/null || true

  echo "== Verifying live site email references =="
  grep -RIn "$NEW_EMAIL\|$OLD_EMAIL" "$WEB_DIR" || true
else
  echo "Site directory not found: $WEB_DIR"
fi

###############################################################################
# Public-Stack repo
###############################################################################

REPO="$HOME/aft-public-software"

if [ -d "$REPO/.git" ]; then
  echo
  echo "== Updating Public-Stack repo =="
  cd "$REPO"

  grep -RIl "$OLD_EMAIL" . \
    --exclude-dir=.git \
    --exclude='*.tar' \
    --exclude='*.tar.gz' \
    --exclude='*.tgz' \
    --exclude='*.zip' \
    | while read -r f; do
        echo "Updating $f"
        sed -i "s#$OLD_EMAIL#$NEW_EMAIL#g" "$f"
      done

  git status --short

  if ! git diff --quiet; then
    git add .
    git commit -m "Update public contact email"
    git push
  else
    echo "No repo changes to commit."
  fi
else
  echo "Repo not found: $REPO"
fi

echo
echo "DONE."
echo "Public email now set to:"
echo "  $NEW_EMAIL"
