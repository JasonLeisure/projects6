function LocationForm() {
    return (
      <div class="row">
        <div class="offset-3 col-6">
          <div class="shadow p-4 mt-4">
            <h1>Create a new location</h1>
            <form id="create-location-form">
              <div class="form-floating mb-3">
                <input placeholder="Name" required type="text" name="name" id="name" class="form-control">
                <label for="name">Name</label>
              </div>
              <div class="form-floating mb-3">
                <input placeholder="Room count" required type="number" name="room_count" id="room_count" class="form-control">
                <label for="room_count">Room count</label>
              </div>
              <div class="form-floating mb-3">
                <input placeholder="City" required type="text" name="city" id="city" class="form-control">
                <label for="city">City</label>
              </div>
              <div class="mb-3">
                <select required name="state" id="state" class="form-select">
                  <option selected value="">Choose a state</option>
                </select>
              </div>
              <button class="btn btn-primary">Create</button>
            </form>
          </div>
        </div>
      </div>
    );
  }
