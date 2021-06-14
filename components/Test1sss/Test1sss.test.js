import React from "react";
import "@testing-library/jest-dom";
import { render } from "@testing-library/react";
import Test1sss from "./";
describe("<Test1sss />", () => {
  let component;
  beforeEach(() => {
    component = render(<Test1sss />);
  });
  test("should render", () => {
    component.getByText("Test1sss");
  });
});