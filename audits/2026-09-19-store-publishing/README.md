# Store publishing audit: Truxon / Freightex → what DQFile needs

Read-only audit of `/home/ike/work/truxon`, `/home/ike/work/truxon-wt`,
`/home/ike/work/freightex` (nothing written there). Goal: learn how the two
existing Unilogistix apps publish to app stores, then say exactly what the
founder must create so Team DQF can publish the DQFile.ai driver app under
his existing Apple/Google accounts, without touching Truxon's or Freightex's
signing material (F-036/F-049).

**Bottom line up front:** neither Truxon nor Freightex actually publishes to
an app store today. Truxon ships Android by self-hosted OTA (signed GitHub
Releases, no Play Store at all) and has never uploaded an iOS build past a
local TestFlight-ready `.ipa` sitting on a Mac. Freightex is mid-setup for
its *own* separate Apple/Play accounts and hasn't shipped either. There is no
App Store Connect API key, no Google Play service account, and no fastlane
anywhere in either repo. DQFile's Expo/EAS app starts from a cleaner position
than either of them, but it also means there is no existing automation to
copy — only lessons and one existing Apple team to reuse.

---

## 1. Apple — App Store Connect / Developer account

**No App Store Connect API key (.p8) exists in either repo.** No `fastlane/`
directory, no `Fastfile`, no `.github/workflows/*ios*` step that signs or
uploads anything. Grep for `.p8`, `issuer`, `ASC API`, `match` turned up only
prose *mentioning* that such a key would be needed, never one that exists.

**Truxon** (`mobile/docs/IOS_RELEASE.md`, `vault/Memory/ios-build-state.md`):
- Apple Developer Program: **paid Individual, "Ilker Yildiz"**, Team ID
  **`PUBHTUQGH4`** (read off `project.pbxproj` / a signed archive, not
  invented — `DEVELOPMENT_TEAM = PUBHTUQGH4` is set on all six Runner build
  configs). Provisioning profile for `com.truxon.truxonCompanion` expires
  **2027-08-27**.
- Bundle id: `com.truxon.truxonCompanion`. Signing style: **Automatic**
  (`CODE_SIGN_STYLE = Automatic`), not fastlane match, not manual profiles.
- Process is entirely manual/local: a Mac (`ikemac`, the only macOS box on
  the tailnet) runs `flutter build ios`/`build-ios.sh ipa`, producing a
  signed `.ipa`. Upload is **Transporter, by hand** — no `xcrun altool`, no
  CI upload step. `IOS_RELEASE.md` says outright: *"Unattended rack
  automation is Fastlane + an App Store Connect API `.p8` + an unlocked
  login keychain + a self-hosted GitHub runner on that Mac. None of
  `fastlane/`, an `ios-testflight.yml`, or a Mac on the tailnet [as a CI
  runner] exists yet."*
- The one CI iOS job (`.github/workflows/ios-build.yml`) only proves the app
  **compiles** (`flutter build ios --release --no-codesign`) — no signing
  credentials in CI at all, by design.
- TestFlight has never actually happened — the `.ipa` was built and signed
  locally (2026-08-26) but the doc explicitly says push is dead (no
  `GoogleService-Info.plist`), the app has "never run on an iOS device or
  simulator" as of the audit doc, and a later vault note says it *did* then
  run on a real iPhone once. No evidence of an actual App Store Connect
  build upload or TestFlight distribution to real testers.
- Registering a new device via CLI is documented as the one thing
  `xcodebuild -allowProvisioningUpdates` **cannot** do without an ASC API
  key — i.e. Truxon itself doesn't have one yet either.

**Freightex** (`docs/IOS_RELEASE.md`, `mobile/STORE_SUBMISSION.md`):
- Explicitly **its own** Apple Developer and App Store Connect records —
  "Release through its own Apple Developer and App Store Connect records,"
  not Truxon's.
- Checked-in Xcode project records team **`PUBHTUQGH4`** (the same Truxon
  team id) as a placeholder/inherited value; the doc tells the release owner
  to *verify it against the current authorized Apple account* before
  shipping — i.e. this may need to change to Freightex's own team once one
  exists, and is flagged as unverified.
- Apple Team ID is meant to live in OpenBao: `freightex/platform/deploy/APPLE_TEAM_ID`
  (path only, confirmed by grep of `docs/STORE_LISTING.md`; I did not and
  cannot read its value, and it isn't reachable with the dqfile-scoped
  token anyway).
- Signing again manual/local Mac + Transporter/Xcode Organizer — same
  pattern as Truxon, no fastlane, no CI signing.
- No TestFlight build has shipped; the release doc is a not-yet-executed
  procedure ("Before submitting metadata, resolve source/listing drift...").

**Conclusion for Apple:** there is exactly **one** real, paid Apple Developer
account documented anywhere in these repos — Truxon's, team `PUBHTUQGH4`,
owned by the founder personally ("Ilker Yildiz"). Freightex intends to get
its *own* separate account (per F-036-style separation) but that account's
existence isn't confirmed here, only a vault path reserved for its team id.
No ASC API key exists for either.

## 2. Google Play

**No Play Developer API service-account JSON exists or is referenced by path
anywhere.** No fastlane `supply`, no `gradle-play-publisher` plugin config
in either `build.gradle.kts`, no CI job that uploads to Play.

**Truxon does not ship on Google Play at all.** `mobile/RELEASES.md`, first
line: *"Installed tablets check for a new version on every launch and offer
to update — **no Play Store**, no thumb drive."* Distribution is:
- A public GitHub repo `turkyildiz/truxon-releases` holding APKs +
  `latest.json` (Ed25519-signed manifest: versionCode/versionName/apkUrl/
  sha256/rolloutPct/sig).
- OTA signing key: Ed25519 PEM, generated with `openssl genpkey`, **stored
  in the owner's KeePassXC vault**, exported to `/dev/shm` only at release
  time and shredded after (`TRUX_OTA_SIGNING_KEY`).
- Upload keystore: `~/truxon-upload.jks` / `truxon-release.jks`, referenced
  from `android/key.properties` (gitignored). Per
  `deploy/secrets/INVENTORY.md`, the real .jks file and its store/key
  passwords are meant to be vaulted in **KeePassXC** under
  `Truxon/Mobile-Signing` (entries: `release-signing`,
  `OTA-manifest-signing-key`, `truxon-release-keystore`), with a copy on the
  NAS (`release-signing/signing-*.tar.gz`) and the live signing keystore
  living on `lynxdev` (a Linux box) — **not OpenBao**. Truxon's whole secrets
  story for mobile signing runs through a `.kdbx` file plus NAS backups.
- There **is** a `play` Gradle flavor (`./build-apk.sh play` →
  `app-play-release.aab`) that strips OTA/`REQUEST_INSTALL_PACKAGES` for a
  hypothetical Play submission, and an original design doc
  (`docs/design-trux-companion-app.md`, "K17") planned "App Store + Google
  Play from day one" with "Apple Developer org + Google Play Console org"
  as an accounts line-item — but nothing in the repo shows a Play Console
  listing was ever actually created or used. The `play` flavor looks built
  in case that plan resumes, not evidence it happened.

**Freightex** is heading toward real Play Console use but hasn't shipped:
- `mobile/setup-release-key.sh` generates `android/freightex-release.jks`
  (alias `freightex`, RSA 4096) + matching `android/key.properties` from one
  password prompt; explicitly told to "keep it in the manager" (a password
  manager, not named which) and never commit it.
- `mobile/STORE_SUBMISSION.md` — App identity/signing section — says the app
  was *forked from Truxon and initially carried Truxon's native identity*;
  this was corrected to `com.freightex.driver` on both platforms specifically
  because shipping Truxon's identifier would make Android treat a Freightex
  install as an **update to Truxon Companion and replace it**. It flags
  explicitly: **"Freightex needs its own signing keystore... An Android
  app's signing key cannot be changed after the first Play upload without
  key rotation, so this is a decision to get right once."**
- `frontend/api/android-assetlinks.js` serves a Digital Asset Links file for
  `com.freightex.driver` sourced from `DRIVER_ANDROID_SHA256`
  ("Play app signing SHA-256 certificate fingerprint... **supplied from Play
  Console App Integrity at release**") — this implies a real Play Console
  app entry is planned/expected once released, using **Play App Signing**
  (Google holds the upload key's counterpart), but the env var is
  unpopulated in what I read and there's no evidence a Play Console listing
  exists yet.
- `docs/STORE_LISTING.md` and `mobile/STORE_SUBMISSION.md` describe the Play
  Console Location-permissions declaration form, Data Safety answers, and
  review-notes text to submit — all prose for a submission that, per
  `RELEASES.md`, is "not shipped app behavior" yet.

**Conclusion for Google Play:** neither app has a confirmed live Play
Console listing. No Play Developer API service account exists anywhere. Each
app's Android signing keystore is generated locally by a one-shot script and
kept in a password manager (Truxon: KeePassXC `.kdbx`; Freightex: "the
manager," unspecified but same pattern) plus NAS backup for Truxon — never
in OpenBao for either. Truxon distributes Android exclusively via self-hosted
OTA, bypassing Play entirely.

## 3. Expo/EAS vs. bare Flutter — and what DQFile already has

**Truxon and Freightex are both bare Flutter apps** (`pubspec.yaml`, native
`ios/`/`android/` projects, CocoaPods, Gradle Kotlin DSL) — no Expo, no React
Native. Grep for `expo`/`eas.json`/`@expo/` in both repos returned nothing
real (the only naive hits were false positives from "export"/"release"
substrings). Their entire iOS/Android build tooling (`build-ios.sh`,
`build-apk.sh`, Podfile, Xcode project) is Flutter-native and does not
transfer to an Expo project at all — nothing to reuse there except the
*policy* lessons above (bundle-id-must-differ, keystore-can't-move-later,
etc.).

**DQFile's driver app already exists and is Expo/React Native**
(`/home/ike/work/dqfile/mobile`, `expo-router`, `eas.json`, `app.json`).
Current state, read directly (no secrets):
- iOS `bundleIdentifier`: **`ai.dqfile.driver`**
- Android `package`: **`ai.dqfile.driver`**
- `app.json extra.eas.projectId` is still the placeholder
  **`"REPLACE_WITH_EAS_PROJECT_ID"`** — no EAS project has been linked yet.
- `eas.json` has `build.production.ios.simulator: false`,
  `android.buildType: "app-bundle"` (an .aab, correct for Play), and an
  empty `submit.production: {}` — the EAS Submit config (where an ASC API
  key path / Play service-account JSON path would eventually go) is
  unconfigured.
- No collision with Truxon (`com.truxon.truxonCompanion`) or Freightex
  (`com.freightex.driver`) — DQFile's identifiers are already distinct and
  already namespaced under the company's own domain, which is the right
  shape per Freightex's own lesson above.

**Implication:** DQFile does not need to decide Expo vs. bare RN — that
choice is already made and already in a better position (managed EAS
Build/Submit, one bundle id already chosen and non-colliding) than either
sibling app. What's missing is entirely on the account/credential side: an
EAS project link, and the Apple/Google credentials EAS Submit needs.

## 4. Founder decisions on record about app identity

- **F-036** (company separation) and **F-037** (secrets only in OpenBao) are
  cited in `dqfile/CLAUDE.md` as law for this repo; `dqfile/TEAM.md` records
  the team's authority as founder direction **F-039** (Team DQF creation,
  2026-09-18).
- Freightex's `STORE_SUBMISSION.md` is the clearest existing founder-adjacent
  decision on identity: **per-company app entries are required** — each
  company gets its own bundle id/package name and its own signing keystore,
  explicitly because sharing an identifier makes one app silently overwrite
  another on a driver's phone, and because Android signing keys can't be
  rotated after first upload. This is a strong precedent for DQFile: it must
  not reuse Truxon's or Freightex's identifiers, keystores, or Apple team —
  and per Freightex's own STORE_LISTING.md it already doesn't (`ai.dqfile.driver`
  vs `com.truxon.*` / `com.freightex.*`).
- Truxon's original design doc (`docs/design-trux-companion-app.md`, "K17")
  records an early founder-level decision that store accounts are "Apple
  Developer org + Google Play Console org" — i.e. **organization** accounts,
  not personal — though what actually got enrolled (per `ios-build-state.md`)
  was a **paid Individual** Apple account under the founder's own name,
  not an org. No document says whether a Google Play Console account (org or
  individual) was ever actually created for Truxon or Freightex; I found no
  confirmation either way, only the unexercised plan and the unpopulated
  `DRIVER_ANDROID_SHA256`/asset-links plumbing.
- I found no document stating whether the founder wants DQFile under the
  *same* Apple Developer account as Truxon (team `PUBHTUQGH4`) as a second
  app entry, or under a brand-new account. This is a reserved decision per
  `dqfile/CLAUDE.md` ("Record reserved decisions... external identity... do
  not assume them") and is called out below as an open question for the
  founder, not assumed.

## 5. What exists in DQFile's OpenBao today

Using `ops/bao/dqbao` (the least-privilege `dqfile-maestro` token — never
the ops token) to **list key names only**, no values read:

```
dqbao list ""              -> app/  fireworks/  health/  postmark/  vercel/
dqbao list mobile          -> (none: HTTP 404)
dqbao list mobile/apple    -> (none: HTTP 404)
dqbao list mobile/google   -> (none: HTTP 404)
dqbao list platform        -> (none: HTTP 404)
dqbao list platform/deploy -> (none: HTTP 404)
```

**Nothing store-related exists yet under `dqfile/` in OpenBao.** No
`mobile/`, `mobile/apple/`, `mobile/google/`, or `platform/deploy/` path is
present. This is a clean slate — there is nothing to accidentally collide
with Truxon's or Freightex's material, and nothing to migrate.

## 6. Recommendation — exact founder to-do list

None of this can reuse Truxon's or Freightex's signing keys, keystores, or
Play/OTA infrastructure (F-036/F-049). Truxon's Apple **team** (`PUBHTUQGH4`)
is a personal paid-Individual Apple ID; whether DQFile becomes a second app
under that same team or gets a brand-new Apple Developer account is a
reserved decision — flagging it as **Q1** below rather than assuming it.

**Founder must create/decide, in order:**

1. **Q1 — Apple account choice (decide first):** either (a) add
   `ai.dqfile.driver` as a new App ID under the existing team `PUBHTUQGH4`
   (fastest — no new $99/yr, but ties DQFile's App Store presence to the
   founder's personal Truxon developer identity), or (b) enroll a separate
   Apple Developer account/org for DQFile ("Team DQF" / Unilogistix org),
   consistent with the org-account intent in Truxon's original K17 plan and
   with F-036 separation. Freightex chose (b)-style ("its own Apple
   Developer and App Store Connect records"); recommend the same for
   consistency, but this is the founder's call.
2. **Register the App ID** `ai.dqfile.driver` in whichever Apple Developer
   account is chosen, with capabilities DQFile actually needs (push only if/
   when notifications are added — the current app.json declares none;
   Associated Domains is already needed for `applinks:dqfile.ai` /
   `applinks:www.dqfile.ai`, which must be enabled on the App ID).
3. **Create a new App Store Connect API key** scoped to DQFile's needs — a
   key with the **App Manager** role (enough for EAS Submit to upload builds
   and manage TestFlight; avoid Admin) is the standard EAS Submit
   requirement. Founder downloads the `.p8` once from App Store Connect
   (Users and Access → Keys) — Apple only allows one download ever — and
   hands me: the Key ID, Issuer ID, and the `.p8` file (never as chat/pasted
   text). I store the `.p8` content in OpenBao at a new path, e.g.
   `dqfile/mobile/apple/ASC_API_KEY_P8` (+ `KEY_ID`, `ISSUER_ID` fields or
   sibling keys), via `dqbao put` — never in git, never in `eas.json`
   directly (EAS also supports uploading the key straight into EAS's own
   encrypted credential store via `eas credentials`, which may be simpler
   than round-tripping through OpenBao — worth deciding together).
4. **Create an App Store Connect app record** for `ai.dqfile.driver` (name
   "DQFile.ai Driver" or similar) — needed before any TestFlight/EAS Submit
   upload can land.
5. **Google Play: create a new, dedicated Google Cloud service account**
   for the Play Developer API (in whichever Google Cloud project backs the
   Play Console the founder uses/creates for DQFile — do not reuse a
   Truxon/Freightex GCP project if one exists for them; none was confirmed
   to exist in the repos I read). Grant it access in Play Console → Users
   and permissions, with the minimum role EAS Submit needs (Release manager
   on the DQFile app, not Admin). Download its JSON key once and hand it to
   me the same secure way as the `.p8` — I store it at e.g.
   `dqfile/mobile/google/PLAY_SERVICE_ACCOUNT_JSON` in OpenBao (or in EAS's
   own credential store).
6. **Register the app in Google Play Console** with package
   `ai.dqfile.driver`, using **Play App Signing** (let Google hold the
   signing key, as Freightex's assetlinks plumbing already assumes) rather
   than Truxon's self-managed-keystore pattern — this avoids ever needing a
   password-manager-held `.jks` file at all, which is the single biggest
   operational risk item in both sibling apps' setups (a lost/leaked
   keystore = a fleet-wide re-key, per Truxon's own inventory notes).
7. **Create the EAS project** (`eas init` from `dqfile/mobile`, run by
   whoever holds Expo org access) and replace the `REPLACE_WITH_EAS_PROJECT_ID`
   placeholder in `app.json` — this is a code change I can make once an EAS
   account/org for DQFile exists; founder needs to say whether EAS should be
   under his personal Expo account or a new "Unilogistix"/"Team DQF" Expo
   org.
8. **Privacy policy URL + App Privacy / Data Safety answers** — Apple and
   Google both require these before review; DQFile handles driver PII
   (license numbers, medical status per `dqfile/CLAUDE.md`) so this needs
   real legal-reviewed text, not placeholder copy, before submission —
   flagging this as a blocker the same way Freightex's own docs flag privacy
   policy / listing drift as a pre-submission gate.

**What I (Maestro) can then automate, once the founder hands over the items
above, without ever touching Truxon/Freightex material:**
- Store the `.p8`, Key ID, Issuer ID, and Play service-account JSON in
  OpenBao under `dqfile/mobile/apple/*` and `dqfile/mobile/google/*` (or push
  them straight into EAS's credential store, whichever the founder prefers)
  via `dqbao put` — values only ever read from stdin, never printed or
  committed.
- Update `dqfile/mobile/app.json`'s `extra.eas.projectId` and `eas.json`'s
  `submit.production` block to reference the new credentials.
- Run `eas build --platform ios|android --profile production` and
  `eas submit` for DQFile builds, and manage TestFlight/Play internal
  testing tracks for `ai.dqfile.driver` — entirely inside DQFile's own Apple/
  Google app records, never adjacent to Truxon's `com.truxon.truxonCompanion`
  or Freightex's `com.freightex.driver` entries.
- Maintain DQFile's own store listing text (description, privacy answers,
  screenshots) the same way Freightex maintains `docs/STORE_LISTING.md` —
  I can draft this file in `dqfile/docs/` once the founder confirms the
  Apple-account and legal-copy decisions above.

## Sources read (paths only, no secret values)

- `truxon/mobile/docs/IOS_RELEASE.md`, `truxon/mobile/RELEASES.md`,
  `truxon/mobile/README.md`, `truxon/mobile/setup-release-key.sh` (not
  present — n/a; used `build-apk.sh`/`build-ios.sh` prose instead)
- `truxon/.github/workflows/ios-build.yml`, `android-review.yml`
- `truxon/vault/Memory/ios-build-state.md`, `mac-dev-box.md`
- `truxon/deploy/secrets/INVENTORY.md`,
  `truxon/vault/Specs/SECRETS_INVENTORY_NAMES.json` (names only)
- `truxon/docs/design-trux-companion-app.md` (K17 store-distribution section)
- `truxon/mobile/android/app/build.gradle.kts`
- `freightex/docs/IOS_RELEASE.md`, `freightex/docs/MOBILE_CI.md`,
  `freightex/docs/STORE_LISTING.md`
- `freightex/mobile/STORE_SUBMISSION.md`, `RELEASES.md`,
  `setup-release-key.sh`, `publish-release.sh`,
  `android/app/build.gradle.kts`
- `freightex/frontend/api/android-assetlinks.js`
- `dqfile/mobile/README.md`, `app.json`, `eas.json`
- `dqfile/ops/bao/dqbao` (read for mechanism), `dqbao list` outputs above
- `dqfile/CLAUDE.md`, `dqfile/TEAM.md` (F-036/F-037/F-039 references)

No secret values were read or printed at any point. No files were modified
in `truxon`, `truxon-wt`, or `freightex`. No login attempts were made against
Apple or Google.
